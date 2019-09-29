import re

from abc import ABCMeta, abstractmethod
from operator import attrgetter
from model import Point2d, Segment2d, Street


class AbstractCommand:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = None

    @abstractmethod
    def execute(self):
        pass


class AddStreetCommand(AbstractCommand):

    def __init__(self, street, points):
        ''' 
            street: [string]  street name
            points: [list of Point2d] coordinates that delimit the street segments
        '''
        self.name = 'add street'

        self.street = street
        self.points = points

    def execute(self, db):
        '''
            db: [dictionary of ([string] street, [list of Point2d] points)]
        '''
        if self.street in db:
            raise Exception('Invalid command. Street %s has already been added. Use "c" to change.' % self.street)

        if (len(self.points) <= 1):
            raise Exception('Invalid command. A street requires at least two points.')

        db[self.street] = self.points

        return (False, None)


class UpdateStreetCommand(AbstractCommand):

    def __init__(self, street, points):
        ''' 
            street: [string] street name
            points: [list of Point2d] coordinates that delimit the street segments
        '''
        self.name = 'update street'

        self.street = street
        self.points = points

    def execute(self, db):
        '''
            db: [dictionary of ([string] street, [list of Point2d] points)]
        '''
        if not self.street in db:
            raise Exception('Invalid command. Street %s does not exist in the database. Use "a" to add.' % self.street)

        db[self.street] = self.points

        return (False, None)


class RemoveStreetCommand(AbstractCommand):

    def __init__(self, street):
        '''
            street: [string] street name
        '''
        self.name = 'remove street'
        self.street = street

    def execute(self, db):
        '''
            db: [dictionary of ([string] street, [list of Point2d] points)]
        '''
        if not self.street in db:
            raise Exception('Invalid command. Street %s does not exist int the database.' % self.street)

        del db[self.street]

        return (False, None)


class GenerateCommand(AbstractCommand):

    def __init__(self):
        self.name = 'generate graph'

    def execute(self, db):
        '''
            db: [dictionary of ([string] street, [list of Point2d] points)]
        '''
        if not db:
            raise Exception('Must not see this! Invalid command. The street database is empty.')

        streets = [Street(value[0], value[1]) for value in db.iteritems()]
        intersections = self.find_intersections(streets)
        vertices, edges, labels, label_count = self.generate_graph(streets)

        v_out = "V = {\n"
        for vertex, label in labels.iteritems():
            v_out += " %s: %10s\n" % (label, vertex)
        v_out += "}"

        e_out = "E = {\n"
        for i, edge in enumerate(edges):
            e_out += " <%s,%s>" % (edge[0], edge[1])
            if i < len(edges) - 1:
                e_out += ","
            e_out += "\n"
        e_out += "}"

        output = "%s\n%s\n" % (v_out, e_out)

        return (True, output)

    def find_intersections(self, streets):
        intersections = {}
        strseen = {}
        for str1 in streets:
            for str2 in streets:

                if str1 == str2:
                    continue

                key1 = max(str1.name, str2.name)
                key2 = min(str1.name, str2.name)

                if key1 in strseen and key2 in strseen[key1]:
                    continue
                else:
                    strseen[key1] = {key2: True}

                for seg1 in str1.segments:
                    for seg2 in str2.segments:

                        # skip fully overlapping segments
                        if seg1 == seg2:
                            continue

                        is_ix, ix = seg1.intersect(seg2)
                        if is_ix:
                            ix_key = str(ix)
                            if ix_key not in intersections:
                                intersections[ix_key] = (ix, [])

                            if seg1 not in intersections[ix_key][1]:
                                intersections[ix_key][1].append(seg1)
                                seg1.add_ix(ix)
                            if seg2 not in intersections[ix_key][1]:
                                intersections[ix_key][1].append(seg2)
                                seg2.add_ix(ix)

        return intersections

    def generate_graph(self, streets):

        vs = []
        es = []

        labels = {}
        label_count = 1
        for street in streets:
            for seg in street.segments:

                # does not execute if no intersections exist
                # if endpoints are included in the graph will be as a result of
                # being part of other segments that contain intersections
                if not seg.intersections:
                    continue

                points = list(seg.intersections)
                points.extend([seg.ep1, seg.ep2])
                points = list(set(points))
                points = sorted(points, key=attrgetter('x', 'y'))

                for p in points:
                    if p not in labels:
                        vs.append(p)
                        labels[p] = str(label_count)
                        label_count += 1

                for i in range(len(points) - 1):
                    edge = (labels[points[i]], labels[points[i + 1]])
                    es.append(edge)
        # remove duplicates added by overlapping edges
        es = list(set(es))
        return vs, es, labels, label_count


class CmdParser:
    def __init__(self):
        self.re_add_update = re.compile(
            r"^[ \t]*(a|c) \"([A-Za-z ]+)\" ((?:[ \t]*\([ \t]*-?[1-9][0-9]*[ \t]*,[ \t]*-?[ \t]*[1-9][0-9]*[ \t]*\))+)[ \t]*$",
            re.IGNORECASE)
        self.re_remove = re.compile(r"^[ \t]*(r) \"([A-Za-z ]+)\"[ \t]*$", re.IGNORECASE)
        self.re_generate = re.compile(r"^[ \t]*(g)[ \t]*$", re.IGNORECASE)
        self.re_coord_str = r"(\([ \t]*(-?\d+)[ \t]*,[ \t]*(-?\d+)[ \t]*\))"

    def parse_add_update(self, match):

        command = match.group(1)
        street = match.group(2)
        coordinates = match.group(3)

        points = []
        for i in re.finditer(self.re_coord_str, coordinates):
            point = Point2d(int(i.group(2)), int(i.group(3)))
            points.append(point)

        if (command == 'a'):
            return AddStreetCommand(street, points)
        elif (command == 'c'):
            return UpdateStreetCommand(street, points)
        else:
            # this should not happen
            raise Exception("Parse error. Command should be 'a' or 'c'")

    def parse_remove(self, match):
        command = match.group(1)
        street = match.group(2)

        if (command == 'r'):
            return RemoveStreetCommand(street)
        else:
            # this should not happen
            raise Exception("Parse error. Command should be 'r'")

    def parse_generate(self, match):
        command = match.group(1)

        if (command == 'g'):
            return GenerateCommand()
        else:
            # this should not happen
            raise Exception("Parse error. Command should be 'g'")

    def parse(self, cmd_str):
        m = filter(lambda m: m != None,
                   [regex.match(cmd_str) for regex in [self.re_add_update, self.re_remove, self.re_generate]])
        if m:
            m = m[0]
            command = {
                'a': lambda m: self.parse_add_update(m),
                'c': lambda m: self.parse_add_update(m),
                'r': lambda m: self.parse_remove(m),
                'g': lambda m: self.parse_generate(m)
            }[m.group(1)](m)
            return command;
        else:
            raise Exception("Error: Incorrect command format")

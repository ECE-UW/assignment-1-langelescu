
import math

from operator import attrgetter

EPSILON = 0.0001

class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other):
        d = math.sqrt((self.ep2.x - other.ep1.x) ** 2 + (self.ep2.y - other.ep1.y) ** 2)
        if d < EPSILON:
            return 0
        else:
            return d

    def __str__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)

    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if not isinstance(other, Point2d):
            return NotImplemented

        return abs(self.x - other.x) < EPSILON and abs(self.y - other.y) < EPSILON
    
    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __hash__(self):
        return hash(str(self))

class Segment2d:

    def __init__(self, p1, p2):
        '''
        p1: Point2d object representing the first endpoint of the segment
        p2: Point2d object representing the second endpoint of the segment 
        '''

        self.ep1 = p1
        self.ep2 = p2
        self.intersections = []

    def orient(self, point):
        cp = (self.ep2.y - self.ep1.y) * (point.x - self.ep2.x) - (self.ep2.x - self.ep1.x) * (point.y - self.ep2.y)

        if(abs(cp) < EPSILON):
            return 0
        elif cp > 0:
            return 1
        else:
            return -1

    def contains(self, point):
        orient = self.orient(point)
        xbt = min(self.ep1.x, self.ep2.x) <= point.x and point.x <= max(self.ep1.x, self.ep2.x)
        ybt = min(self.ep1.y, self.ep2.y) <= point.y and point.y <= max(self.ep1.y, self.ep2.y)
       
        if (orient == 0 and xbt and ybt):
            return True
        else:
            return False

    def compute_intersection(self, other):

        # Regular case: no overlap. Solve for (x,y)
        # y = mx + b
        # m = dy/dx

        if (self.ep2.x - self.ep1.x == 0 and other.ep2.y - other.ep1.y == 0):
            x = self.ep1.x
            y = other.ep1.y
            ix = Point2d(x, y)
            return ix

        if (other.ep2.x - other.ep1.x == 0 and self.ep2.y - self.ep1.y == 0):
            x = other.ep1.x
            y = self.ep1.y
            ix = Point2d(x, y)

        if (self.ep2.x - self.ep1.x == 0):
            x = self.ep1.x
            y = (other.ep2.y - other.ep1.y)*(x - other.ep1.x)/(other.ep2.x - other.ep1.x) + other.ep1.y
            ix = Point2d(x, y)
            return ix

        if (other.ep2.x - other.ep1.x == 0):
            x = other.ep1.x
            y = (self.ep2.y - self.ep1.y)*(x - self.ep1.x)/(self.ep2.x - self.ep1.x) + self.ep1.y
            ix = Point2d(x, y)
            return ix

        if (self.ep2.y - self.ep1.y == 0):
            y = self.ep1.y
            x = (y - other.ep1.y)*(other.ep2.x - other.ep1.x)/(other.ep2.y - other.ep1.y) + other.ep1.x
            ix = Point2d(x, y)
            return ix

        if (other.ep2.y - other.ep1.y == 0):
            y = other.ep1.y
            x = (y - self.ep1.y)*(self.ep2.x - self.ep1.x)/(self.ep2.y - self.ep1.y) + self.ep1.x
            ix = Point2d(x, y)
            return ix

        mseg1 = (self.ep2.y - self.ep1.y) / (self.ep2.x - self.ep1.x)
        mseg2 = (other.ep2.y - other.ep1.y) / (other.ep2.x - other.ep1.x)

        bseg1 = self.ep1.y - mseg1 * self.ep1.x
        bseg2 = other.ep1.y - mseg2 * other.ep1.x

        x = (bseg2 - bseg1) / (mseg1 - mseg2)
        y = (mseg1 * bseg2 - mseg2 * bseg1) / (mseg1 - mseg2)

        ix = Point2d(x, y)
        return ix

    def intersect(self, other):
        d1 = self.orient(other.ep1)
        d2 = self.orient(other.ep2)
        d3 = other.orient(self.ep1)
        d4 = other.orient(self.ep2)

        # segments are not collinear, therefore they intersect
        if (((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0))):
            return True, self.compute_intersection(other)

        return False, None

    def add_ix(self, intersection):
        if intersection in self.intersections:
            return

        self.intersections.append(intersection)
        sorted(self.intersections, key=attrgetter('x', 'y'))

    def __str__(self):
        return '%s-%s' % (str(self.ep1), str(self.ep2))
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if not isinstance(other, Segment2d):
            return NotImplemented

        return ((self.ep1 == other.ep1) or (self.ep1 == other.ep2)) and \
            ((self.ep2 == other.ep1) or (self.ep2 == other.ep2))

    def __ne__(self, other):
        if not isinstance(other, Segment2d):
            return NotImplemented

        return not self.__eq__(self, other)


class Street:

    def __init__(self, name, points):
        ''' name:   character string representing the name of the streets
            points: list of Point2d objects that delimit the street segments
        '''

        self.name = name
        self.ep1 = points[1]
        self.ep2 = points[-1]
        self.points = points
        self.segments = []
        for p1, p2 in zip(points, points[1:]):
            self.segments.append(Segment2d(p1, p2))

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __str__(self):
        return self.name + " " + str(self.segments)

    def __repr__(self):
        return str(self)

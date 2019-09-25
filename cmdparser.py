import re

from abc import ABCMeta, abstractmethod
from model import Point2d

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

        return (True, 'OK')        

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
        
        return (True, 'OK')

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

        return (True, 'OK')

class GenerateCommand(AbstractCommand):

    def __init__(self):
        self.name = 'generate graph'

    def execute(self, db):
        '''
            db: [dictionary of ([string] street, [list of Point2d] points)]
        '''
        if not db:
            raise Exception('Invalid command. The street database is empty.')

        return (True, 'OK')

class CmdParser:
    def __init__(self):
        self.re_add_update = re.compile("^[ \t]*(a|c) \"([A-Za-z ]+)\" ((?:[ \t]*\([ \t]*-?[1-9][0-9]*[ \t]*,[ \t]*-?[ \t]*[1-9][0-9]*[ \t]*\))+)[ \t]*$", re.IGNORECASE)
        self.re_remove = re.compile("^[ \t]*(r) \"([A-Za-z ]+)\"[ \t]*$", re.IGNORECASE)
        self.re_generate = re.compile("^[ \t]*(g)[ \t]*$", re.IGNORECASE)
        self.re_coord_str = "((-?\d+),(-?\d+))"
    
    def parse_add_update(self, match):
        command = match.group(1)
        street = match.group(2)
        points = []
        for i in re.finditer(self.re_coord_str, match.group(3)):
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


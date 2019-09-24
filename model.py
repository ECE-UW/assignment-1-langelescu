
class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if not isinstance(other, Point2d):
            return NotImplemented

        # TODO: Update this to support floating point coordinates!
        return (self.x == other.x) and (self.y == other.y)
    
    def __neq__(self, other):
        return not self.__eq__(self, other)    

class Segment2d:

    def __init__(self, p1, p2):
        '''
        p1: Point2d object representing the first endpoint of the segment
        p2: Point2d object representing the second endpoint of the segment 
        '''

        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '%s - %s' % (str(self.p1), str(self.p2))
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if not isinstance(other, Segment2d):
            return NotImplemented

        return ((self.p1 == other.p1) or (self.p1 == other.p2)) and \
            ((self.p2 == other.p1) or (self.p2 == other.p2))

class Street:

    def __init__(self, name, points):
        ''' name:   character string representing the name of the streets
            points: list of Point2d objects that delimit the street segments
        '''

        self.name = name
        self.points = points

    def segments(self):
        ''' Returns list of Segment2d object that define a street'''
        
        pass

    def __str__(self):
        return ''

class Intersection:

    def __init__(self, coord, segments):
        ''' coord:    Point2d coordinate representing an intersection of streets and segments
            streets:  List of Street objects representing streets that intersect at coord
            segments: List of Segment2d of the streets, correlated by index, that intersect at coord
        '''                
        
        self.coord = coord
        self.streets = []
        self.segments = []

    def __str__(self):
        return str(self.coord)

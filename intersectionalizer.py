
class Intersectionalizer:

    def __init__(self):
        pass

    @staticmethod
    def intersect(seg1, seg2):
        return False

    @staticmethod
    def orient(sep1, sep2, p):
        ''' Returns the direction of point p relative to the segment with endpoints
        sep1 and sep2

            sep1: [Point2d] segment endpoint 1
            sep2: [Point2d] segment endpoint 2
            p   : [Point2d] point p

            Returns:
                -1 : direction is counterclockwise
                 0 : p is collinear with sep1 and sep2
                 1 : direction is clockwise
        '''

        dir = (sep2.y - sep1.y) * (p.x - sep2.x) - \
                (sep2.x - sep1.x) * (p.y - sep2.y)

        # Points are collinear
        if dir == 0 : return 0
        # Points turn clockwise
        elif dir > 0: return 1
        # Points turn counterclockwise
        else: return -1

    @staticmethod
    def exists_intersection(seg1, seg2):
        ''' Verifies the intersection of two 2d segments
            
            seg1: [Segment2d] first segment
            seg2: [Segment2d] second segment

            Returns:
                True if the segments intersect and False otherwise
        '''

        dseg1_seg2ep1 = Intersectionalizer.orient(seg1.ep1, seg1.ep2, seg2.ep1)
        dseg1_seg2ep2 = Intersectionalizer.orient(seg1.ep1, seg1.ep2, seg2.ep2)
        dseg2_seg1ep1 = Intersectionalizer.orient(seg2.ep1, seg2.ep2, seg1.ep1)
        dseg2_seg1ep2 = Intersectionalizer.orient(seg2.ep1, seg2.ep2, seg1.ep2)

        if ((dseg1_seg2ep1 != dseg1_seg2ep2) and (dseg2_seg1ep1 != dseg2_seg1ep2)):
            return True

        if (dseg1_seg2ep1 == 0 and seg1.contains_point(seg2.ep1)): return True
        if (dseg1_seg2ep2 == 0 and seg1.contains_point(seg2.ep2)): return True
        if (dseg2_seg1ep1 == 0 and seg2.contains_point(seg1.ep1)): return True
        if (dseg2_seg1ep1 == 0 and seg2.contains_point(seg1.ep2)): return True

        return False

        
    @staticmethod
    def compute_intersection(seg1, seg2):
        if not Intersectionalizer.exists_intersection(seg1, seg2):
            return []




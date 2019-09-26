import unittest

from model import Segment2d, Point2d

class ModelTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_contained_point_is_detected(self):
        
        sep11 = Point2d(0,2) ; sep12 = Point2d(5,2)
        seg1 = Segment2d(sep11, sep12)

        sep21 = Point2d(4,2) ; sep22 = Point2d(7,2)
        seg2 = Segment2d(sep21, sep22)

        self.assertTrue(seg1.contains_point(seg2.ep1))
        self.assertFalse(seg1.contains_point(seg2.ep2))

        self.assertFalse(seg2.contains_point(seg1.ep1))
        self.assertTrue(seg2.contains_point(seg1.ep2))

    def test_uncontained_point_is_rejected(self):
        
        sep11 = Point2d(0,2) ; sep12 = Point2d(3,2)
        seg1 = Segment2d(sep11, sep12)

        sep21 = Point2d(4,2) ; sep22 = Point2d(6,2)
        seg2 = Segment2d(sep21, sep22)

        self.assertFalse(seg1.contains_point(seg2.ep1))
        self.assertFalse(seg1.contains_point(seg2.ep2))

        self.assertFalse(seg2.contains_point(seg1.ep1))
        self.assertFalse(seg2.contains_point(seg1.ep2))

if __name__ == '__main__':
    unittest.main()


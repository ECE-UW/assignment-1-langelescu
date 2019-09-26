
import unittest

from intersectionalizer import Intersectionalizer
from model import Point2d, Segment2d

class IntersectionalizerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_detect_intersection_on_cross_intersecting_segments(self):
        
        p1 = Point2d(1,4) ; p2 = Point2d(1,1)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(0,2) ; r2 = Point2d(3,2)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertTrue(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertTrue(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertTrue(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertTrue(Intersectionalizer.exists_intersection(seg22, seg12))

    def test_detect_intersection_on_tx_intersecting_segments(self):
        
        p1 = Point2d(1,4) ; p2 = Point2d(1,1)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(1,2) ; r2 = Point2d(3,2)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertTrue(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertTrue(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertTrue(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertTrue(Intersectionalizer.exists_intersection(seg22, seg12))

    def test_detect_intersection_on_ty_intersecting_segments(self):
        
        p1 = Point2d(1,4) ; p2 = Point2d(1,1)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(0,2) ; r2 = Point2d(3,2)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertTrue(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertTrue(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertTrue(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertTrue(Intersectionalizer.exists_intersection(seg22, seg12))

    def test_detect_intersection_on_shared_point_intersecting_segments(self):

        p1 = Point2d(1,4) ; p2 = Point2d(1,2)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(1,2) ; r2 = Point2d(3,2)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertTrue(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertTrue(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertTrue(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertTrue(Intersectionalizer.exists_intersection(seg22, seg12))

    def test_detect_intersection_on_shared_point_ycollinear_segments(self):
        
        p1 = Point2d(1,4) ; p2 = Point2d(1,2)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(1,2) ; r2 = Point2d(1,1)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertTrue(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertTrue(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertTrue(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertTrue(Intersectionalizer.exists_intersection(seg22, seg12))
       
    def test_detect_intersection_on_shared_point_xcollinear_segments(self):
        
        p1 = Point2d(0,2) ; p2 = Point2d(2,2)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(2,2) ; r2 = Point2d(5,2)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertTrue(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertTrue(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertTrue(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertTrue(Intersectionalizer.exists_intersection(seg22, seg12))

    def test_reject_intersection_on_ycollinear_and_disjoint_segments(self):

        p1 = Point2d(0,2) ; p2 = Point2d(3,2)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(4,2) ; r2 = Point2d(6,2)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertFalse(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertFalse(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertFalse(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertFalse(Intersectionalizer.exists_intersection(seg22, seg12))
    
    def test_reject_intersection_on_xcollinear_and_disjoint_segments(self):
        
        p1 = Point2d(1,5) ; p2 = Point2d(1,2)
        seg11 = Segment2d(p1, p2)
        seg12 = Segment2d(p2, p1)

        r1 = Point2d(1,7) ; r2 = Point2d(1,10)
        seg21 = Segment2d(r1, r2)
        seg22 = Segment2d(r2, r1)

        self.assertFalse(Intersectionalizer.exists_intersection(seg11, seg21))
        self.assertFalse(Intersectionalizer.exists_intersection(seg21, seg11))
        self.assertFalse(Intersectionalizer.exists_intersection(seg12, seg22))
        self.assertFalse(Intersectionalizer.exists_intersection(seg22, seg12))

if __name__ == '__main__':
    unittest.main()

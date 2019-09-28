import unittest

from model import Segment2d, Point2d, Street

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

        self.assertTrue(seg1.contains(seg2.ep1))
        self.assertFalse(seg1.contains(seg2.ep2))

        self.assertFalse(seg2.contains(seg1.ep1))
        self.assertTrue(seg2.contains(seg1.ep2))

    def test_uncontained_point_is_rejected(self):
        
        sep11 = Point2d(0,2) ; sep12 = Point2d(3,2)
        seg1 = Segment2d(sep11, sep12)

        sep21 = Point2d(4,2) ; sep22 = Point2d(6,2)
        seg2 = Segment2d(sep21, sep22)

        self.assertFalse(seg1.contains(seg2.ep1))
        self.assertFalse(seg1.contains(seg2.ep2))

        self.assertFalse(seg2.contains(seg1.ep1))
        self.assertFalse(seg2.contains(seg1.ep2))

    def test_2d_points_are_equal_within_tolerance(self):

        p1 = Point2d(0.234523, 0.22222)
        p2 = Point2d(0.234521, 0.22225)

        self.assertTrue(p1 == p2)

    def test_2d_points_are_not_equal_outside_tolerance(self):

        p1 = Point2d(0.234523, 0.22222)
        p2 = Point2d(0.234400, 0.22222)

        self.assertFalse(p1 == p2)

    def test_2d_segments_are_not_equal(self):
        
        seg1 = Segment2d(Point2d(0,0), Point2d(4,4))
        seg2 = Segment2d(Point2d(0,4), Point2d(4,0))

        self.assertFalse(seg1 == seg2)


    def test_2d_segments_are_equal(self):

        seg1 = Segment2d(Point2d(1,5), Point2d(2,6))
        seg2 = Segment2d(Point2d(1,5), Point2d(2,6))
        seg3 = Segment2d(Point2d(2,6), Point2d(1,5))

        self.assertTrue(seg1 == seg2)
        self.assertTrue(seg1 == seg3)

    def test_2d_intersecting_segments_do_not_contain_endpoints(self):

        seg1 = Segment2d(Point2d(0,0), Point2d(4,4))
        seg2 = Segment2d(Point2d(0,4), Point2d(4,0))

        self.assertTrue(seg1.contains(seg1.ep1))
        self.assertTrue(seg1.contains(seg1.ep2))
        self.assertFalse(seg1.contains(seg2.ep1))
        self.assertFalse(seg1.contains(seg2.ep2))

        self.assertTrue(seg2.contains(seg2.ep1))
        self.assertTrue(seg2.contains(seg2.ep2))
        self.assertFalse(seg2.contains(seg1.ep1))
        self.assertFalse(seg2.contains(seg1.ep2))

    def test_2d_intersection_segments_intersect_in_one_point(self):

        seg1 = Segment2d(Point2d(0,0), Point2d(4,4))
        seg2 = Segment2d(Point2d(0,4), Point2d(4,0))

        do_intersect, ixs = seg1.intersect(seg2)
        self.assertTrue(do_intersect)
        self.assertTrue(ixs == Point2d(2,2)) 
    
    def test_2d_intersection_segments_have_full_overlap(self):
        
        seg1 = Segment2d(Point2d(1,1), Point2d(3,3))
        seg2 = Segment2d(Point2d(3,3), Point2d(1,1))

        self.assertTrue(seg1 == seg2)
        self.assertTrue(seg2 == seg1)

    def test_2d_intersection_segment_have_partial_internal_overlap(self):
        
        seg1 = Segment2d(Point2d(1,1), Point2d(3,3))
        seg2 = Segment2d(Point2d(2,2), Point2d(4,4))

        do_intersect, ixs = seg1.intersect(seg2)
        self.assertTrue(do_intersect)

    def test_street_constructor_builds_correct_segments(self):

        points = [Point2d(2, -1), Point2d(2, 2), Point2d(5, 5), Point2d(5, 6), Point2d(3, 8)]
        segments = [Segment2d(Point2d(2, -1), Point2d(2,2)), Segment2d(Point2d(2,2), Point2d(5,5)), 
            Segment2d(Point2d(5,5), Point2d(5,6)), Segment2d(Point2d(5,6), Point2d(3,8))]

        wstreet = Street("Weber Street", points)
        self.assertItemsEqual(wstreet.segments, segments)

if __name__ == '__main__':
    unittest.main()



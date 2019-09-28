
import unittest

from cmdparser import CmdParser
from model import Point2d, Segment2d 

class CmdParserTest(unittest.TestCase):
    
    def setUp(self):
        self.db = {
                'Weber Street'  :  [ Point2d(2, -1), Point2d(2,2), Point2d(5,5), Point2d(5,6), Point2d(3,8)],
                'King Street S' :  [Point2d(4,2), Point2d(4,8)],
                'Davenport Road': [Point2d(1,4), Point2d(5,8)]
                }
        
        self.db_empty = { }

    def tearDown(self):
        self.db = None
        self.db_empty = None

    def test_correct_input_addupdate_street_command_parses_successfully(self):
        """ Tests that valid input for the 'Add street' command is parsed correctly """

        parser = CmdParser()
        
        i11 = r'a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)'
        command = parser.parse(i11)
        i11segments = [Segment2d(Point2d(2, -1), Point2d(2,2)), Segment2d(Point2d(2,2), Point2d(5,5)), 
            Segment2d(Point2d(5,5), Point2d(5,6)), Segment2d(Point2d(5,6), Point2d(3,8))]
        
        self.assertEqual(command.name, 'add street')
        self.assertEqual(command.street, 'Weber Street')
        self.assertItemsEqual(self.db[command.street], command.points)
        
        i12 = r' a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)'
        command = parser.parse(i12)
        self.assertEqual(command.name, 'add street')
        self.assertEqual(command.street, 'Weber Street')
        self.assertItemsEqual(self.db[command.street], command.points)
        
        i13 = r'  a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8) '
        command = parser.parse(i13)
        self.assertEqual(command.name, 'add street')
        self.assertEqual(command.street, 'Weber Street')
        self.assertItemsEqual(self.db[command.street], command.points)
        
        i21 = r'c "Weber Street" (4,2) (4,8)'
        command = parser.parse(i21)
        self.assertEqual(command.name, 'update street')
        self.assertEqual(command.street, 'Weber Street')
        self.assertItemsEqual([Point2d(4,2), Point2d(4,8)], command.points) 
        
        i22 = r' c "Weber Street" (4,2) (4,8)'
        command = parser.parse(i22)
        self.assertEqual(command.name, 'update street')
        self.assertEqual(command.street, 'Weber Street')
        self.assertItemsEqual([Point2d(4,2), Point2d(4,8)], command.points)

        i23 = r'  c "Weber Street" (4,2) (4,8) '
        command = parser.parse(i23)
        self.assertEqual(command.name, 'update street')
        self.assertEqual(command.street, 'Weber Street')
        self.assertItemsEqual([Point2d(4,2), Point2d(4,8)], command.points)
    
    def test_correct_input_remove_street_command_parses_sucessfully(self):
        
        parser = CmdParser()
        
        i1 = r'r "Davenport Road"'
        command = parser.parse(i1)
        self.assertEqual(command.name, 'remove street')
        self.assertEqual(command.street, 'Davenport Road')

        i2 = r' r "Davenport Road"'
        command = parser.parse(i2)
        self.assertEqual(command.name, 'remove street')
        self.assertEqual(command.street, 'Davenport Road')

        i3 = r'  r "Davenport Road" '
        command = parser.parse(i3)
        self.assertEqual(command.name, 'remove street')
        self.assertEqual(command.street, 'Davenport Road')

    def test_correct_input_generate_command_parses_successfully(self):

        parser = CmdParser()
        
        i1 = r'g'
        command = parser.parse(i1)
        self.assertEqual(command.name, 'generate graph')

        i2 = r' g'
        command = parser.parse(i2)
        self.assertEqual(command.name, 'generate graph')
        
        i3 = r'  g '
        command = parser.parse(i3)
        self.assertEqual(command.name, 'generate graph')

    def test_command_add_update_generate_segments_correctly(self):

        parser = CmdParser()
        
        i11 = r'a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)'
        i11points = [Point2d(2,-1), Point2d(2,2), Point2d(5,5), Point2d(5,6), Point2d(3,8)]
        i11segments = [Segment2d(Point2d(2, -1), Point2d(2,2)), Segment2d(Point2d(2,2), Point2d(5,5)), 
            Segment2d(Point2d(5,5), Point2d(5,6)), Segment2d(Point2d(5,6), Point2d(3,8))]
        
        db = {}
        command = parser.parse(i11)
        command.execute(db)

        self.assertEqual(command.name, 'add street')
        self.assertEqual(db[command.street].name, 'Weber Street')
        self.assertItemsEqual(db[command.street].segments, i11segments)

if __name__ == '__main__':
    unittest.main()


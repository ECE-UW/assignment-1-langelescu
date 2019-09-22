
import unittest

from cmdparser import CmdParser

class CmdParserTest(unittest.TestCase):

    def test_correct_input_addupdate_street_command_parses_successfully(self):
        """ Tests that valid input for the 'Add street' command is parsed correctly """

        parser = CmdParser()
        
        valid_input1_weber = r'a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)'
        valid_input2_king  = r'c "Weber Street" (4,2) (4,8)'
        
        command = parser.parse(valid_input1_weber)
        status, message, cmd = command.execute()

        self.assertTrue(status)
        self.assertEqual(message, 'OK')
        self.assertEqual(cmd, 'add street')

        command = parser.parse(valid_input2_king)
        status, message, cmd = command.execute()

        self.assertTrue(status)
        self.assertEqual(message, 'OK')
        self.assertEqual(cmd, 'update street')
        
    def test_correct_input_remove_street_command_parses_sucessfully(self):
        
        parser = CmdParser()
        valid_input = r'r "Davenport Road"'
        
        command = parser.parse(valid_input)
        status, message, cmd = command.execute()

        self.assertTrue(status)
        self.assertEqual(message, 'OK')
        self.assertEqual(cmd, 'remove street')

    def test_correct_input_generate_command_parses_successfully(self):

        parser = CmdParser()
        valid_input = r'g'

        command = parser.parse(valid_input)
        status, message, cmd = command.execute()

        self.assertTrue(status)
        self.assertEqual(message, 'OK')
        self.assertEqual(cmd, 'generate graph')

if __name__ == '__main__':
    unittest.main()


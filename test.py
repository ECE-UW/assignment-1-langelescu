import unittest

from cmdparser import CmdParser


class A1ece650Tests(unittest.TestCase):

    def test_scenario1(self):
        i1 = r'a "Weber Street" (2,-1)(2,2) (5,5) (5,6) (3,8)'
        i2 = r'a "King Street S" (4,2) (4,8)'
        i3 = r'a "Davenport Road" (1,4) (5,8)'
        i4 = r'c "Weber Street" (2,1) (2,2)'
        i5 = r'r "King Street S"'
        i6 = r'g'

        parser = CmdParser()
        db = {}

        c1 = parser.parse(i1)
        c2 = parser.parse(i2)
        c3 = parser.parse(i3)
        c4 = parser.parse(i4)
        c5 = parser.parse(i5)

        c1.execute(db)
        c2.execute(db)
        c3.execute(db)
        c4.execute(db)
        c5.execute(db)

        c6 = parser.parse(i6)
        has_out, out = c6.execute(db)
        if has_out:
            print out

        self.assertTrue(True)

    def test_scenario2(self):
        i1 = r'a "up and across st" (0,0) (10,10)'
        i2 = r'a "StreetB" (0,10)(10,0)'
        i3 = 'g'

        parser = CmdParser()
        db = {}

        c1 = parser.parse(i1)
        c2 = parser.parse(i2)

        c1.execute(db)
        c2.execute(db)

        c3 = parser.parse(i3)
        has_out, out = c3.execute(db)
        if has_out:
            print out

        self.assertTrue(True)

    def test_scenario3(self):
        i1 = r'a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)'
        i2 = r'a "King Street S" (3,2) (4,8)'
        i3 = r'a "Davenport Road" (0,0) (5,8)'
        i4 = r'g'

        parser = CmdParser()
        db = {}

        c1 = parser.parse(i1)
        c2 = parser.parse(i2)
        c3 = parser.parse(i3)
        c4 = parser.parse(i4)

        c1.execute(db)
        c2.execute(db)
        c3.execute(db)
        has_out, out = c4.execute(db)
        if has_out:
            print out

        self.assertTrue(True)

    def test_scenario4(self):
        i1 = r'a "Amphitheatre Prkw" (2,-1)(2,2) (5,5) (5,6) (3,8)'
        i2 = r'c "amphitheatre PRKW" (0,0)(4,0)'
        i3 = r'a "One Infinite Loop" (3,0)(5,0)'
        i4 = r'g'

        parser = CmdParser()
        db = {}

        c1 = parser.parse(i1)
        c2 = parser.parse(i2)
        c3 = parser.parse(i3)
        c4 = parser.parse(i4)

        c1.execute(db)
        c2.execute(db)
        c3.execute(db)
        has_out, out = c4.execute(db)
        if has_out:
            print out

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

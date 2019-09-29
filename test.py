import unittest

from cmdparser import CmdParser


class A1ece650Tests(unittest.TestCase):

    def test_scenario1(self):
        i1 = r'a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)'
        i2 = r'a "King Street S" (4,2) (4,8)'
        i3 = r'a "Davenport Road" (1,4) (5,8)'

        parser = CmdParser()
        db = {}

        c1 = parser.parse(i1)
        c2 = parser.parse(i2)
        c3 = parser.parse(i3)

        c1.execute(db)
        c2.execute(db)
        c3.execute(db)

        i4 = 'g'
        c4 = parser.parse(i4)
        has_out, out = c4.execute(db)
        if has_out:
            print out

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

"Tests for scrip."
import unittest

from script import Round


class TestRoundClass(unittest.TestCase):
    "Unit test of Round."
    def test_ax(self):
        "Test A X."
        _round = Round("A X")
        self.assertEqual(_round.my_choice(), 2)
        self.assertEqual(_round.score(), 3)

    def test_ay(self):
        "Test A Y"
        _round = Round("A Y")
        self.assertEqual(_round.my_choice(), 0)
        self.assertEqual(_round.score(), 4)

    def test_az(self):
        "Test A Z."
        _round = Round("A Z")
        self.assertEqual(_round.my_choice(), 1)
        self.assertEqual(_round.score(), 8)

if __name__ == '__main__':
    unittest.main()
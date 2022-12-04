"Test Round class from scrip."
import unittest

from script import Round


class TestRoundClass(unittest.TestCase):
    def test_ax(self):
        round = Round("A X")
        self.assertEqual(round.my_choice(), 2)
        self.assertEqual(round.score(), 3)

    def test_ay(self):
        round = Round("A Y")
        self.assertEqual(round.my_choice(), 0)
        self.assertEqual(round.score(), 4)

    def test_az(self):
            round = Round("A Z")
            self.assertEqual(round.my_choice(), 1)
            self.assertEqual(round.score(), 8)

if __name__ == '__main__':
    unittest.main()
"Test Round class from scrip."
import unittest

from script import TuningTrouble


class TestTuningTrouble(unittest.TestCase):
    "Tests for TuningTrouble"

    def test_example(self):
        _example = """nppdvjthqldpwncqszvftbrmjlhg"""
        _impl = TuningTrouble(_example)
        self.assertEqual(_impl.answer(), 23)

if __name__ == '__main__':
    unittest.main()
pass
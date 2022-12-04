"Test Round class from scrip."
import unittest

from script import CampCleanup


class TestCampCleanup(unittest.TestCase):
    "Tests for RucksackReorganization"

    def test_example(self):
        _example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        _impl = CampCleanup(_example.splitlines())
        self.assertEqual(_impl.score(), 2)


if __name__ == '__main__':
    unittest.main()

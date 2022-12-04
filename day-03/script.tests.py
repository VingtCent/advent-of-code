"Test Round class from scrip."
import unittest

from script import Rucksack, RucksackReorganization


class TestRucksackReorganization(unittest.TestCase):
    "Tests for RucksackReorganization"
    def test_example(self):
        _example = """vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw"""
        _reorg = RucksackReorganization(_example.splitlines())
        self.assertEqual(_reorg.score(), 157)

class TestRucksack(unittest.TestCase):
    "Tests for Rucksack"
    def test_a(self):
        self.assertEqual(Rucksack('aa').score(), 1)

    def test_Z(self):
        self.assertEqual(Rucksack('ZZ').score(), 52)

if __name__ == '__main__':
    unittest.main()

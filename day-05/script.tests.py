"Test Round class from scrip."
import unittest

from script import SupplyStacks


class TestSupplyStacks(unittest.TestCase):
    "Tests for RucksackReorganization"

    def test_example(self):
        _example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
        _impl = SupplyStacks(_example.splitlines())
        self.assertEqual(_impl.answer(), 'MCD')

if __name__ == '__main__':
    unittest.main()
pass
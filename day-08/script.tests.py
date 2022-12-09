"Test Round class from scrip."
import unittest

from script import NoSpaceLeftOnDevice


class TestSupplyStacks(unittest.TestCase):
    "Tests for RucksackReorganization"
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """30373
25512
65332
33549
35390"""

    def test_answer1(self):        
        _impl = NoSpaceLeftOnDevice(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 21)

    def test_answer2(self):      
        _impl = NoSpaceLeftOnDevice(self.example.splitlines())
        self.assertEqual(_impl.answer2(), 8)

if __name__ == '__main__':
    unittest.main()
pass
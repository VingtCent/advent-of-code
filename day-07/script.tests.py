"Test Round class from scrip."
import unittest

from script import NoSpaceLeftOnDevice


class TestSupplyStacks(unittest.TestCase):
    "Tests for RucksackReorganization"
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    def test_answer1(self):        
        _impl = NoSpaceLeftOnDevice(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 95437)

    def test_answer2(self):      
        _impl = NoSpaceLeftOnDevice(self.example.splitlines())
        self.assertEqual(_impl.answer2(), 'd')

if __name__ == '__main__':
    unittest.main()
pass
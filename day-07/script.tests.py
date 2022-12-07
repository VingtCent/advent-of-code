"Test Round class from scrip."
import unittest

from script import NoSpaceLeftOnDevice


class TestSupplyStacks(unittest.TestCase):
    "Tests for RucksackReorganization"

    def test_example(self):
        _example = """$ cd /
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
        _impl = NoSpaceLeftOnDevice(_example.splitlines())
        self.assertEqual(_impl.answer(), 95437)

if __name__ == '__main__':
    unittest.main()
pass
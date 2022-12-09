"Test scrip file."
import unittest
from script import RopeBridge


class TestRopeBridge(unittest.TestCase):
    "Tests for RopeBridge"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = RopeBridge(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 13)

    def test_answer2(self):
        "Test answer for part 2."
        example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
        _impl = RopeBridge(example2.splitlines())
        self.assertEqual(_impl.answer2(), 36)


if __name__ == "__main__":
    unittest.main()

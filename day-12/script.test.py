"Test scrip file."
import unittest
from script import HillClimbingAlgorithm


class TestHillClimbingAlgorithm(unittest.TestCase):
    "Tests for HillClimbingAlgorithm"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = HillClimbingAlgorithm(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 31)

    def test_answer2(self):
        "Test answer for part 2."
        _impl = HillClimbingAlgorithm(self.example.splitlines())
        self.assertEqual(_impl.answer2(), None)


if __name__ == "__main__":
    unittest.main()

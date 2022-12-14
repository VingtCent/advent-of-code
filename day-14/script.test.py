"Test scrip file."
import unittest
from script import RegolithReservoir


class TestRegolithReservoir(unittest.TestCase):
    "Tests for RegolithReservoir"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = RegolithReservoir(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 24)

    def test_answer2(self):
        "Test answer for part 2."
        _impl = RegolithReservoir(self.example.splitlines())
        self.assertEqual(_impl.answer2(), 93)


if __name__ == "__main__":
    unittest.main()

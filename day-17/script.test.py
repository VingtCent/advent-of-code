"Test scrip file."
import unittest
from script import PyroclasticFlow


class TestPyroclasticFlow(unittest.TestCase):
    "Tests for PyroclasticFlow"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = PyroclasticFlow(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 3068)

    def test_answer2(self):
        "Test answer for part 2."
        _impl = PyroclasticFlow(self.example.splitlines())
        self.assertEqual(_impl.answer2(), None)


if __name__ == "__main__":
    unittest.main()

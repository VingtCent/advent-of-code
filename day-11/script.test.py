"Test scrip file."
import unittest
from script import MonkeyInTheMiddle


class TestMonkeyInTheMiddle(unittest.TestCase):
    "Tests for MonkeyInTheMiddle"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = MonkeyInTheMiddle(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 10605)

    def test_answer2(self):
        "Test answer for part 2."
        _impl = MonkeyInTheMiddle(self.example.splitlines())
        self.assertEqual(_impl.answer2(), None)


if __name__ == "__main__":
    unittest.main()

"Test scrip file."
import unittest
from script import DistressSignal


class TestDistressSignal(unittest.TestCase):
    "Tests for DistressSignal"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = DistressSignal(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 13)

    def test_answer2(self):
        "Test answer for part 2."
        _impl = DistressSignal(self.example.splitlines())
        self.assertEqual(_impl.answer2(), 140)


if __name__ == "__main__":
    unittest.main()

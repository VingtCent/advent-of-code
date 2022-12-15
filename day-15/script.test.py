"Test scrip file."
import unittest
from script import BeaconExclusionZone


class TestBeaconExclusionZone(unittest.TestCase):
    "Tests for RegolithReservoir"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.example = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = BeaconExclusionZone(self.example.splitlines())
        self.assertEqual(_impl.answer1(10), 26)

    def test_answer2(self):
        "Test answer for part 2."
        _impl = BeaconExclusionZone(self.example.splitlines())
        self.assertEqual(_impl.answer2(), 93)


if __name__ == "__main__":
    unittest.main()

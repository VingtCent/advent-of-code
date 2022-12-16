"Test scrip file."
import unittest
from script import ProboscideaVolcanium


class TestBeaconExclusionZone(unittest.TestCase):
    "Tests for ProboscideaVolcanium"

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        #         self.example = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
        # Valve BB has flow rate=13; tunnels lead to valves CC, AA
        # Valve CC has flow rate=2; tunnels lead to valves DD, BB
        # Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
        # Valve EE has flow rate=3; tunnels lead to valves FF, DD
        # Valve FF has flow rate=0; tunnels lead to valves EE, GG
        # Valve GG has flow rate=0; tunnels lead to valves FF, HH
        # Valve HH has flow rate=22; tunnel leads to valve GG
        # Valve II has flow rate=0; tunnels lead to valves AA, JJ
        # Valve JJ has flow rate=21; tunnel leads to valve II"""
        self.example = """Valve AA has flow rate=0; tunnels lead to valves BB
Valve BB has flow rate=1; tunnels lead to valves AA"""

    def test_answer1(self):
        "Test answer for part 1."
        _impl = ProboscideaVolcanium(self.example.splitlines())
        self.assertEqual(_impl.answer1(), 28)

    def test_answer2(self):
        "Test answer for part 2."
        _impl = ProboscideaVolcanium(self.example.splitlines())
        self.assertEqual(_impl.answer2(), None)


if __name__ == "__main__":
    unittest.main()

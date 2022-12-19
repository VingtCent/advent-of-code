"Advent of code day 16."

from dataclasses import dataclass
import re
from typing import Callable, Tuple, Type


def main():
    "Main."
    handle = open(r"./day-16/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = ProboscideaVolcanium(_lines)
    print("Answer 1:", _impl.answer1())
    _impl = ProboscideaVolcanium(_lines)
    print("Answer 2:", _impl.answer2())


class ProboscideaVolcanium:
    "Impl class."

    def __init__(self, lines: list[str]) -> None:
        self.valves = dict()
        line_pattern = re.compile(
            r"^Valve (?P<valve>[A-Z]+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<destinations>([A-Z]+,?\s*)*)$"
        )
        self.rates = dict()
        self.leads = dict()
        for line in lines:
            match = line_pattern.match(line)
            self.rates[match.group("valve")] = int(match.group("rate"))
            self.leads[match.group("valve")] = [
                l.strip() for l in match.group("destinations").strip().split(",")
            ]

    def _max(self, valve: str, time: int, predecessor: str | None):
        destinations = [d for d in self.leads[valve] if d != predecessor]
        if not destinations:
            return (self.rates[valve] * (time - 1), 1)

        valve_opened = False
        result = 0
        time_left = time        
        while time_left > 0 and (destinations or not valve_opened):
            max_valve = valve if not valve_opened else None
            max_valve_value = self.rates[valve] * (time_left - 1) if not valve_opened else -1
            max_valve_time = 1 if not valve_opened else 0
            for destination in destinations:
                value, valve_time = self._max(destination, time_left - 1, valve)
                if max_valve is None or value > max_valve_value:
                    max_valve = destination
                    max_valve_value = value
                    max_valve_time = valve_time + 2
            result += max_valve_value
            time_left -= max_valve_time
            if max_valve == valve:
                valve_opened = True
            else:
                destinations.remove(max_valve)

        return (result, time - time_left)

    def answer1(self):
        "Returns answer to part1."
        return self._max("AA", 30, None)[0]

    def answer2(self):
        "Returns answer to part 2."
        return None


if __name__ == "__main__":
    main()

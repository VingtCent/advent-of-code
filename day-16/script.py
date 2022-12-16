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


@dataclass
class _Valve:
    name: str
    rate: int
    destinations: list[str]


@dataclass
class _MaxResult:
    time_spent: int
    value: int


class ProboscideaVolcanium:
    "Impl class."

    def __init__(self, lines: list[str]) -> None:
        self.valves = dict()
        line_pattern = re.compile(
            r"^Valve (?P<valve>[A-Z]+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<destinations>([A-Z]+,?\s*)*)$"
        )
        for line in lines:
            match = line_pattern.match(line)
            self.valves[match.group("valve")] = _Valve(
                match.group("valve"),
                int(match.group("rate")),
                match.group("destinations").split(", "),
            )

    def _max(
        self, valve: Type[_Valve], time: int, predecessor: str | None
    ) -> _MaxResult:
        valve_result = _MaxResult(1, (time-1) * valve.rate)
        if time == 1:
            return valve_result
        else:
            result = _MaxResult(0, lambda x: x * 0)
           
            results: dict[str, _MaxResult] = dict()
            results[valve.name] = valve_result
            for key in [d for d in valve.destinations if d != predecessor]:
                results[key] = self._max(self.valves[key], time - 1, valve.name)
            while time >= 1 and results:
               

                keys = list(results.keys())
                max_key = keys.pop(0)
                result[max_key] = self._max(self.valves[max_key], time, valve.name)
                
                for key in keys:
                    if results[key].time_spent > time:
                        result[key] = self._max(self.valves[key], time, valve.name)
                    if results[key].calcul(time) > results[max_key].calcul(time):
                        max_key = key
                
                max_result = results.pop(max_key)
                result.calcul = lambda x: result.calcul(x) + max_result.calcul(
                    x - result.time_spent - 1 if max_key != valve.name else 0
                )
                result.time_spent += max_result.time_spent
                time -= max_result.time_spent

            return result

    def answer1(self):
        "Returns answer to part1."
        return self._max(self.valves["AA"], 30, None).value

    def answer2(self):
        "Returns answer to part 2."
        return None


if __name__ == "__main__":
    main()

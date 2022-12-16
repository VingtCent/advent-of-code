"Advent of code day 15."

import re
from typing import Tuple


def main():
    "Main."
    handle = open(r"./day-15/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = BeaconExclusionZone(_lines)
    print("Answer 1:", _impl.answer1(2000000))
    _impl = BeaconExclusionZone(_lines)
    print("Answer 2:", _impl.answer2(4000000))


class BeaconExclusionZone:
    "Impl class."

    def __init__(self, lines: list[str]) -> None:
        self._sensors = [_Sensor(l) for l in lines]

    def answer1(self, row: int):
        "Returns answer to part1."
        result = set()
        for sensor in self._sensors:
            result.update(sensor.get_detected_positions(row))
        result.difference_update(
            [s.closest_beacon[0] for s in self._sensors if s.closest_beacon[1] == row]
        )
        return len(result)

    def answer2(self, search_area:int):
        "Returns answer to part 2."
        for i in range(search_area+1):
            positions = set(range(0, search_area+1))
            for sensor in self._sensors:
                detected = sensor.get_detected_positions(i)
                positions.difference_update(detected)
                if len(positions)==0:
                    break
            if len(positions) > 0:
                result = (positions.pop(), i)
                break
        return result[0]*4000000 + result[1]


class _Sensor:
    _sensor_pattern = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )

    def __init__(self, line: str) -> None:
        match = _Sensor._sensor_pattern.match(line)
        self.position = (int(match.group(1)), int(match.group(2)))
        self.closest_beacon = (int(match.group(3)), int(match.group(4)))
        self._distance = self._get_distance(self.closest_beacon)

    def get_detected_positions(self, row: int) -> set[int]:
        "Returns absysses of detected positions"
        result = set()
        index = 0
        while self._get_distance((self.position[0] + index, row)) <= self._distance:
            result.add(self.position[0] + index)
            result.add(self.position[0] - index)
            index += 1
        return result

    def _get_distance(self, position: Tuple[int, int]):
        return abs(self.position[0] - position[0]) + abs(self.position[1] - position[1])


if __name__ == "__main__":
    main()

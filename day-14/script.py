"Advent of code day 13."


from typing import Tuple
import re


def main():
    "Main."
    handle = open(r"./day-14/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = RegolithReservoir(_lines)
    print("Answer 1:", _impl.answer1())
    _impl = RegolithReservoir(_lines)
    print("Answer 2:", _impl.answer2())


class RegolithReservoir:
    "Impl class."

    def __init__(self, lines: list[str]) -> None:
        self._start = (500, 0)
        self._occupied_locations = dict()
        section_pattern = re.compile(r"(\d+),(\d+)")
        self._mins = dict()
        self._floor: int | None = None
        for path in lines:
            first = True
            for match in section_pattern.findall(path):
                right = int(match[0])
                down = int(match[1])
                if first:
                    start = (right, down)
                    first = False
                else:
                    end = (right, down)
                    if start[0] != end[0] and start[1] == end[1]:
                        for i in range(
                            min(start[0], end[0]), max(start[0], end[0]) + 1
                        ):
                            self._occupied_locations[(i, start[1])] = None
                            self._add_max(i, start[1])
                    elif start[0] == end[0] and start[1] != end[1]:
                        for i in range(
                            min(start[1], end[1]), max(start[1], end[1]) + 1
                        ):
                            self._occupied_locations[(start[0], i)] = None
                            self._add_max(start[0], i)
                    else:
                        raise ValueError(path)
                    start = end

    def _add_max(self, right, down):
        if right in self._mins:
            self._mins[right] = max(self._mins[right], down)
        else:
            self._mins[right] = down

    def answer1(self):
        "Returns answer to part1."
        index = 0
        while self._put(self._start) is not None:
            index += 1

        return index

    def answer2(self):
        "Returns answer to part 2."
        self._floor = max(self._mins.values()) + 2
        index = 0
        while self._put(self._start) != self._start:
            index += 1
        return index + 1

    def _put(self, point: Tuple[int, int]) -> Tuple[int, int] | None:
        moves = [
            (point[0], point[1] + 1),
            (point[0] - 1, point[1] + 1),
            (point[0] + 1, point[1] + 1),
        ]
        for move in moves:
            if self._can_move(move):
                return self._put(move)
            else:
                if self._flows_out(move):
                    return None
        if not self._flows_out(point):
            self._occupied_locations[point] = None
            return point
        else:
            return None

    def _can_move(self, location: Tuple[int, int]):
        if location in self._occupied_locations:
            return False
        if self._floor is not None:
            return location[1] < self._floor
        return not self._flows_out(location)

    def _flows_out(self, point: Tuple[int, int]):
        if self._floor:
            return False
        return point[0] not in self._mins or point[1] > self._mins[point[0]]


if __name__ == "__main__":
    main()

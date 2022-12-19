"Advent of code day 16."

import re
from typing import Tuple


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
        pass

    def answer1(self):
        "Returns answer to part1."
        return None

    def answer2(self):
        "Returns answer to part 2."
        return None


if __name__ == "__main__":
    main()

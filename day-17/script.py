"Advent of code day 17."

import re
from typing import Tuple


def main():
    "Main."
    handle = open(r"./day-16/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = PyroclasticFlow(_lines)
    print("Answer 1:", _impl.answer1())
    _impl = PyroclasticFlow(_lines)
    print("Answer 2:", _impl.answer2())


class PyroclasticFlow:
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

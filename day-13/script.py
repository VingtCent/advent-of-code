"Advent of code day 13."


from functools import cmp_to_key
from typing import Any


def main():
    "Main."
    handle = open(r"./day-13/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = DistressSignal(_lines)
    print("Answer 1:", _impl.answer1())
    _impl = DistressSignal(_lines)
    print("Answer 2:", _impl.answer2())


class DistressSignal:
    "Impl class."

    def __init__(self, lines: list[str]) -> None:
        self.pairs = []
        for i, line in enumerate(lines):
            match i % 3:
                case 0:
                    line1 = line
                case 1:
                    self.pairs.append(_Pair(i // 3 + 1, line1, line))
                case _:
                    pass

    def answer1(self):
        "Returns answer to part1."
        return sum([p.index for p in self.pairs if p.is_right_order()])

    def answer2(self):
        "Returns answer to part 2."
        lines = [[[2]], [[6]]]
        for pair in self.pairs:
            lines.append(pair.line1)
            lines.append(pair.line2)
        lines.sort(key=cmp_to_key(_Pair.compare))
        return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)


class _Pair:
    def __init__(self, index, line1, line2) -> None:
        self.line1 = _Pair._parse(line1)
        self.line2 = _Pair._parse(line2)
        self.index = index

    @staticmethod
    def _parse(line: str) -> list[Any]:
        result = []
        current_number = ""
        value = line.strip()[1:-1]
        index = 0
        while index < len(value):
            character = value[index]
            if character.isnumeric():
                current_number += character
                index += 1
            elif character == ",":
                if current_number != "":
                    result.append(int(current_number))
                    current_number = ""
                index += 1
            elif character == "[":
                end = index + _Pair._find_end(value[index:])
                result.append(_Pair._parse(value[index : end + 1]))
                index = end + 1
            else:
                raise ValueError("Unknown")
        if current_number != "":
            result.append(int(current_number))
        return result

    @staticmethod
    def _find_end(value: str):
        sub_lists = 0
        for i, character in enumerate(value):
            match character:
                case "]":
                    sub_lists -= 1
                    if sub_lists == 0:
                        return i
                case "[":
                    sub_lists += 1
                case _:
                    pass
        raise ValueError("No end found")

    @staticmethod
    def compare(left, rigth):
        "Compare 2 lines."
        if isinstance(left, int):
            left = [left]
        if isinstance(rigth, int):
            rigth = [rigth]
        for i, left_value in enumerate(left):
            if i >= len(rigth):
                return 1
            rigth_value = rigth[i]
            if isinstance(left_value, int) and isinstance(rigth_value, int):
                if left_value < rigth_value:
                    return -1
                elif left_value > rigth_value:
                    return 1
            else:
                compare = _Pair.compare(left_value, rigth_value)
                if compare != 0:
                    return compare
        if len(left) < len(rigth):
            return -1
        return 0

    def is_right_order(self):
        "Compare line1 with line2 to check order."
        result = _Pair.compare(self.line1, self.line2)
        print(self.line1, self.line2, " = ", result)
        return result < 0


if __name__ == "__main__":
    main()

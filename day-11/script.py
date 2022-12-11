"Advent of code day 11."


import re


def main():
    "Main."
    handle = open(r"./day-11/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = MonkeyInTheMiddle(_lines)
    print("Answer 1:", _impl.answer1())
    print("Answer 2:", _impl.answer2())


class MonkeyInTheMiddle:
    "Impl class."

    def __init__(self, lines) -> None:
        monkeypattern = r"^Monkey (?P<monkey>\d+):\s*Starting items:(?P<items>.*)\n\s*Operation:(?P<operation>.*)\n\s*Test:(?P<test>.*)\n\s*If true: throw to monkey (?P<monkey_true>\d+)\n\s*If false: throw to monkey (?P<monkey_false>\d+)"
        self.monkeys = []
        for i in range(0, len(lines), 7):
            match = re.match(monkeypattern, "\n".join(lines[i : i + 6]))
            if not match:
                raise ValueError("Unable to read monkey")
            items = [int(item.strip()) for item in match.group("items").split(",")]

            operationline = match.group("operation")
            testline = match.group("test")
            monkey_true = int(match.group("monkey_true"))
            monkey_false = int(match.group("monkey_false"))
            self.monkeys.append(
                _Monkey(items, operationline, testline, monkey_true, monkey_false)
            )

    def answer1(self):
        "Returns Answer to part1 problem"
        for i in range(20):
            for monkey in self.monkeys:
                moves = monkey.play()
                for move in moves:
                    self.monkeys[move[0]].add(move[1])
            print("Round", i)
            for j, monkey in enumerate(self.monkeys):
                print("Monkey",j, monkey)
        monkeysinspections = sorted([m.inspections for m in self.monkeys])        
        return monkeysinspections[-2] * monkeysinspections[-1]

    def answer2(self):
        "Answer to part 2."
        return None


class _Monkey:
    def __init__(self, starting_items, operation, test, monkey_true, monkey_false):
        self._items = starting_items
        self._operationline = operation
        self._testline = test
        self._monkey1 = monkey_true
        self._monkey2 = monkey_false
        self.inspections = 0

    def __str__(self) -> str:
        return ', '.join([str(x) for x in self._items])

    def _ops(self, item):
        arg = self._operationline.split()[-1]
        if arg == "old":
            value = item
        else:
            value = int(arg)

        if self._operationline.startswith(" new = old * "):
            return item * value
        elif self._operationline.startswith(" new = old + "):
            return item + value
        else:
            raise ValueError("Unable to read operation")

    def _test(self, item):
        arg = int(self._testline.split()[-1])
        return item % arg == 0

    def play(self):
        "Play a round."
        moves = []
        for item in self._items:
            self.inspections += 1
            item = self._ops(item) // 3
            if self._test(item):
                moves.append((self._monkey1, item))
            else:
                moves.append((self._monkey2, item))
        self._items.clear()
        return moves

    def add(self, item):
        "Add an item to monkey inventory."
        self._items.append(item)


if __name__ == "__main__":
    main()

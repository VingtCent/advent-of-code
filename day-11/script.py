"Advent of code day 11."


from math import prod
import re


def main():
    "Main."
    handle = open(r"./day-11/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = MonkeyInTheMiddle(_lines)
    print("Answer 1:", _impl.answer1())
    _impl = MonkeyInTheMiddle(_lines)
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
                print("Monkey", j, monkey)
        monkeysinspections = sorted([m.inspections for m in self.monkeys])
        return monkeysinspections[-2] * monkeysinspections[-1]

    def answer2(self):
        "Answer to part 2."
        common_modulator = prod(monkey.modulator for monkey in self.monkeys)
        for i in range(1, 10001):
            for monkey in self.monkeys:
                moves = monkey.play(1)
                for move in moves:
                    self.monkeys[move[0]].add(move[1]%common_modulator)
            if i in [1, 50, 100, 500, 1000, 5000, 10000]:
                print("Round", i)
                for j, monkey in enumerate(self.monkeys):
                    print("Monkey", j, "inspected items ", monkey.inspections, "times")
        monkeysinspections = sorted([m.inspections for m in self.monkeys])
        return monkeysinspections[-2] * monkeysinspections[-1]


class _Monkey:
    def __init__(self, starting_items, operation, test, monkey_true, monkey_false):
        self._items = starting_items
        self._monkey1 = monkey_true
        self._monkey2 = monkey_false
        self.inspections = 0

        if operation.startswith(" new = old * old"):
            self._operation = lambda item: item * item
        elif operation.startswith(" new = old * "):
            value = int(operation.split()[-1])
            self._operation = lambda item: item * value
        elif operation.startswith(" new = old + old"):
            self._operation = lambda item: item + item
        elif operation.startswith(" new = old + "):
            value = int(operation.split()[-1])
            self._operation = lambda item: item + value
        else:
            raise ValueError("Unable to read operation")

        self.modulator = int(test.split()[-1])

    def __str__(self) -> str:
        return ", ".join([str(x) for x in self._items])

    def _ops(self, item):
        return self._operation(item)

    def _test(self, item):
        return item % self.modulator == 0

    def play(self, relief=3):
        "Play a round."
        moves = []
        for item in self._items:
            self.inspections += 1
            item = self._ops(item) // relief
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

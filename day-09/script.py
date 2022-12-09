"Advent of code day 9."


def main():
    "Main."
    handle = open(r"./day-09/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = RopeBridge(_lines)
    print("Answer 1:", _impl.answer1())
    print("Answer 2:", _impl.answer2())


class RopeBridge:
    "Impl class."

    def __init__(self, lines) -> None:
        self.moves = [(l.split()[0], int(l.split()[1])) for l in lines]

    def answer1(self):
        "Returns Answer to part1 problem"
        positions = set()
        rope = Rope()

        for move in self.moves:
            for _ in range(0, move[1]):
                positions.add(rope.move(move[0]))

        return len(positions)

    def answer2(self):
        "Answer to part 2."
        positions = set()
        rope = Rope(9)

        for move in self.moves:
            for _ in range(0, move[1]):
                positions.add(rope.move(move[0]))

        return len(positions)


class Rope:
    "Define the behavior of a rope."

    def __init__(self, tails=1) -> None:
        self._elements = [[0, 0]] + [[0, 0] for _ in range(0, tails)]

    @staticmethod
    def _dostep(direction, position):
        match direction:
            case "U":
                position[1] += 1
            case "D":
                position[1] -= 1
            case "R":
                position[0] += 1
            case "L":
                position[0] -= 1
            case _:
                raise ValueError(direction)

    @staticmethod
    def _follow(first, second):
        xdiff = first[0] - second[0]
        ydiff = first[1] - second[1]
        if abs(xdiff) > 1 or abs(ydiff) > 1:
            if xdiff != 0:
                second[0] += xdiff // abs(xdiff)
            if ydiff != 0:
                second[1] += ydiff // abs(ydiff)

    def move(self, direction):
        "Move the rope to one direction."
        Rope._dostep(direction, self._elements[0])
        for i in range(1, len(self._elements)):
            Rope._follow(self._elements[i - 1], self._elements[i])
        return (self._elements[-1][0], self._elements[-1][1])


if __name__ == "__main__":
    main()

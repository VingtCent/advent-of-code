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
        return None


class Rope:
    "Define the behavior of a rope."

    def __init__(self) -> None:
        self._head = [0, 0]
        self._tail = [0, 0]

    @staticmethod
    def _move(direction, position):
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

    def move(self, direction):
        "Move the rope to one direction."
        Rope._move(direction, self._head)
        xdiff = self._head[0] - self._tail[0]
        ydiff = self._head[1] - self._tail[1]
        if abs(xdiff) > 1 or abs(ydiff) > 1:
            if xdiff == 0 or ydiff == 0:
                Rope._move(direction, self._tail)
            else:
                self._tail[0] += xdiff // abs(xdiff)
                self._tail[1] += ydiff // abs(ydiff)
        return (self._tail[0], self._tail[1])


if __name__ == "__main__":
    main()

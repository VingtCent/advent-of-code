"Advent of code day 10."


def main():
    "Main."
    handle = open(r"./day-10/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = CathodeRayTube(_lines)
    print("Answer 1:", _impl.answer1())
    print("Answer 2:", _impl.answer2())


class CathodeRayTube:
    "Impl class."

    def __init__(self, lines) -> None:
        self._commands = lines
        self._xvalue = 1
        self._cycle = 0

    def answer1(self):
        "Returns Answer to part1 problem"
        self._xvalue = 1
        self._cycle = 0
        nextmeasurment = 20
        signalstrength = 0
        for command in [c.split() for c in self._commands]:
            match command[0]:
                case "noop":
                    self._cycle += 1
                case "addx":
                    self._cycle += 2
                    nextvalue = self._xvalue + int(command[1])
                case _:
                    raise ValueError(f"Command {command[0]} not handle")
            if self._cycle >= nextmeasurment:
                signalstrength += nextmeasurment * self._xvalue
                nextmeasurment += 40
            self._xvalue = nextvalue

        return signalstrength

    def _print(self):
        self._cycle += 1
        if (self._xvalue) <= self._cycle % 40 <= (self._xvalue + 2):
            print("#", sep='', end='')
        else:
            print(".", sep='', end='')
        if self._cycle % 40 == 0:
            print("\n", sep='', end='')

    def answer2(self):
        "Answer to part 2."
        self._xvalue = 1
        self._cycle = 0
        print("Display:")
        for command in [c.split() for c in self._commands]:
            match command[0]:
                case "noop":
                    self._print()
                case "addx":
                    for _ in range(0, 2):
                        self._print()
                    self._xvalue = self._xvalue + int(command[1])
                case _:
                    raise ValueError(f"Command {command[0]} not handle")

        return None


if __name__ == "__main__":
    main()

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
        self.commands = lines

    def answer1(self):
        "Returns Answer to part1 problem"
        xvalue = 1
        cycle = 0
        nextmeasurment = 20
        signalstrength = 0
        for command in [c.split() for c in self.commands]:
            match command[0]:
                case "noop":
                    cycle += 1
                case "addx":
                    cycle += 2
                    nextvalue = xvalue + int(command[1])
                case _:
                    raise ValueError(f"Command {command[0]} not handle")
            if cycle >= nextmeasurment:
                signalstrength += nextmeasurment * xvalue
                nextmeasurment += 40
            xvalue = nextvalue

        return signalstrength

    def answer2(self):
        "Answer to part 2."
        return None


if __name__ == "__main__":
    main()

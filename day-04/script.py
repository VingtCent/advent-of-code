"Advent of code day 4."
handle = open(r'./day-04/input', 'r', encoding='UTF8')
_lines = handle.readlines()


class CampCleanup:
    "Camp cleanup class."

    def __init__(self, lines) -> None:
        self.teams = map(Team, lines)

    def score(self):
        "Return nb of teams overlapping."
        return sum(map(lambda t: t.isoverlapping(), self.teams))


class Team:
    "Team of 2 elves"

    def __init__(self, line: str) -> None:
        _split = line.split(',')
        self.elf1 = set(range(int(_split[0].split('-')[0]),
                          int(_split[0].split('-')[1]) + 1))
        self.elf2 = set(range(int(_split[1].split('-')[0]),
                          int(_split[1].split('-')[1]) + 1))

    def isoverlapping(self):
        "Returns true if elf1 or elf2 are overlapping"
        return len(self.elf1.intersection(self.elf2))>0


_cleanup = CampCleanup(_lines)
print(_cleanup.score())

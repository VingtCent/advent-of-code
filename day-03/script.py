"Advent of code day 3."
handle = open(r'./day-03/input', 'r', encoding='UTF8')
_lines = handle.readlines()


class RucksackReorganization:
    "Main class for day 03."

    def __init__(self, lines) -> None:
        self.rucksacks = map(Rucksack, lines)

    def score(self):
        "Return score."
        return sum(map(lambda r: r.score(), self.rucksacks))


class Rucksack:
    "Rucksack as define on advent code description"

    def __init__(self, line) -> None:
        _line = line.strip()
        self.compartments = (_line[:(len(_line)//2)], _line[len(_line)//2:])

    def score(self):
        "return the score of this rucksack"
        _score = 0
        for item in self.compartments[0]:
            if self.compartments[1].find(item) != -1:
                if item.isupper():
                    return ord(item) - ord('A') + 27
                else:
                    return ord(item) - ord('a') + 1
        return _score


_reorg = RucksackReorganization(_lines)
print(_reorg.score())

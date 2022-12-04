"Advent of code day 3."
handle = open(r'./day-03/input', 'r', encoding='UTF8')
_lines = handle.readlines()


class RucksackReorganization:
    "Main class for day 03."

    def __init__(self, lines) -> None:
        self.groups = []
        for _index in range(0, len(lines), 3):
            self.groups.append(Group(lines[_index], lines[_index+1], lines[_index+2]))

    def score(self):
        "Return score."
        return sum(map(lambda r: r.score(), self.groups))


class Group:
    "Groups for step 2"

    def __init__(self, line1, line2, line3) -> None:
        self.elves = (line1.strip(), line2.strip(), line3.strip())

    def score(self):
        "Returns ths score for the group."
        for item in self.elves[0]:
            if self.elves[1].find(item) != -1 and self.elves[2].find(item) != -1:
                if item.isupper():
                    return ord(item) - ord('A') + 27
                else:
                    return ord(item) - ord('a') + 1
        raise Exception("should not happened")

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

"Advent of code day 5."
import re;

def main():
    handle = open(r'./day-06/input', 'r', encoding='UTF8')
    _lines = handle.readlines()
    _cleanup = TuningTrouble(_lines)
    print(_cleanup.answer())


class TuningTrouble:
    "Day 6 implementation"

    def __init__(self, lines) -> None:
       self.input = "".join(lines)

    def answer(self):
        lastCharacters = []
        for index, c in enumerate(self.input):
            
            lastCharacters.insert(0, c)
            if index >= 14:
                lastCharacters.pop()            
                if len(set(lastCharacters)) == 14:
                    return index + 1
            
        return None


if __name__ == '__main__':
    main()
pass


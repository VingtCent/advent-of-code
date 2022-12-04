"Advent of code day 2."
handle = open(r'./day-02/input', 'r', encoding='UTF8')
lines = handle.readlines()

class Round:
    "Define a Rock paperscisor round."
    def __init__(self, line):
        self.opponent_choice = ord(line[0]) - ord('A')
        self.my_choice = ord(line[2]) - ord('X')
    def result(self):
        "Return 0 if defeat, 3 if draw, 6 if win."
        if self.opponent_choice == self.my_choice:
            return 3
        if self.opponent_choice == 0:
            if self.my_choice == 1:
                return 6
            elif self.my_choice == 2:
                return 0
        if self.opponent_choice == 1:
            if self.my_choice == 2:
                return 6
            elif self.my_choice == 0:
                return 0
        if self.opponent_choice == 2:
            if self.my_choice == 0:
                return 6
            elif self.my_choice == 1:
                return 0
    def score(self):
        "Return the score of this round."
        return self.my_choice +1 + self.result()

rounds = map(lambda l:Round(l), lines)
print(sum(map(lambda r: r.score(), rounds)))

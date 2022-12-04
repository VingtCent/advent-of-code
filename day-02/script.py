"Advent of code day 2."
handle = open(r'./day-02/input', 'r', encoding='UTF8')
lines = handle.readlines()


class Round:
    "Define a Rock paperscisor round."

    def __init__(self, line):
        self.opponent_choice = ord(line[0]) - ord('A')
        self.result = (ord(line[2]) - ord('X')) * 3

    def my_choice(self):
        "Calcul my_choice depending of the opponent choice and expected result."
        if self.result == 3:  # draw
            return self.opponent_choice
        elif self.result == 0:  # loose
            return (self.opponent_choice + 2) % 3
        elif self.result == 6:  # win
            return (self.opponent_choice + 1) % 3
        raise Exception("something went wrong")

    def score(self):
        "Return the score of this round."
        return self.my_choice() + 1 + self.result


rounds = map(Round, lines)
print(sum(map(lambda r: r.score(), rounds)))

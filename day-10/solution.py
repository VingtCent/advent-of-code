from dataclasses import dataclass

with open(r"day-10/input") as f:
    inp = [line.strip() for line in f.readlines()]


@dataclass
class State:
    reg: int = 1
    cycle: int = 0
    signals: int = 0
    board: str = ""

    def add(self, val):
        for _ in range(2):
            self.tick()
        self.reg += val

    def noop(self):
        self.tick()

    def tick(self):
        self.cycle += 1
        vals = list(range(20, 221, 40))
        if self.cycle in vals:
            self.signals += self.reg * self.cycle

        hpos = self.cycle % 40
        sprite = list(range(max(self.reg - 1, 0), min(self.reg + 1, 39) + 1))

        if hpos - 1 in sprite:
            self.board += "#"
        elif hpos == 0:
            self.board += "\n"
        else:
            self.board += "."


state = State()
for line in inp:
    if line == "noop":
        state.noop()
    else:
        state.add(int(line.split()[1]))

print(state.signals)
print(state.board)
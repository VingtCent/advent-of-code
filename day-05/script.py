"Advent of code day 5."
import re;

def main():
    handle = open(r'./day-05/input', 'r', encoding='UTF8')
    _lines = handle.readlines()
    _cleanup = SupplyStacks(_lines)
    print(_cleanup.answer())


class SupplyStacks:
    "Camp cleanup class."

    def __init__(self, lines) -> None:
        index = 0
        stackPattern = r"^\s*(\[\w\]\s*)+$"
        stacksLines = []
        while index < len(lines) and re.match(stackPattern, lines[index]):
            stacksLines.append(lines[index])
            index += 1 
        stacksNumberLine = lines[index]
        index+=1

        numberOfStacks = len(stacksNumberLine.split())
        self.stacks = []
        for _ in range(0, numberOfStacks):
            self.stacks.append([])
        
        for line in stacksLines:
            for stack in range(0, numberOfStacks):
                element = line[stack*4 : stack*4 + 4].strip()
                if element:
                    self.stacks[stack].insert(0, element[1])

        movePattern = r"^move (\d+) from (\d+) to (\d+)$"
        while index < len(lines) and not re.match(movePattern, lines[index]):
            index += 1
        self.moveLines = []
        while index < len(lines) and re.match(movePattern, lines[index]):
            self.moveLines.append(lines[index])
            index+=1        

    def answer(self):
        movePattern = r"^move (\d+) from (\d+) to (\d+)$"
        for move in self.moveLines:
            m = re.match(movePattern, move)
            nbofmove = int(m.group(1))
            fromstack = int(m.group(2))
            tostack = int(m.group(3))
            self.stacks[tostack - 1] += self.stacks[fromstack-1][-nbofmove:]
            self.stacks[fromstack-1][-nbofmove:] = []
        result = ''
        for stack in self.stacks:
            result += stack[-1]
        return result


if __name__ == '__main__':
    main()
pass


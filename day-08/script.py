"Advent of code day 8."
import re;

def main():
    handle = open(r'./day-08/input', 'r', encoding='UTF8')
    _lines = handle.readlines()
    _impl = NoSpaceLeftOnDevice(_lines)
    print("Answer 1:", _impl.answer1())
    print("Answer 2:", _impl.answer2())


class NoSpaceLeftOnDevice:
    "Impl class."

    def __init__(self, lines) -> None:
        self.rows = [[int(value) for value in line.strip()] for line in lines]
        self.columns = list(zip(*self.rows))
        
    def answer1(self):        
        result = len(self.rows)*2 + len(self.columns)*2 - 4
        for j in range(1, len(self.rows)-1):
            for i in range(1, len(self.columns)-1):
                currenttree = self.rows[i][j]
                if (not [t for t in self.rows[i][:j] if t >= currenttree]) \
                        or (not [t for t in self.rows[i][j+1:] if t >= currenttree]) \
                        or (not [t for t in self.columns[j][:i] if t >= currenttree]) \
                        or (not [t for t in self.columns[j][i+1:] if t >= currenttree]):
                    result += 1
        return result                

    def answer2(self):                
        return None

if __name__ == '__main__':
    main()
pass


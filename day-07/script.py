"Advent of code day 7."
import re;

def main():
    handle = open(r'./day-07/input', 'r', encoding='UTF8')
    _lines = handle.readlines()
    _cleanup = NoSpaceLeftOnDevice(_lines)
    print(_cleanup.answer())


class NoSpaceLeftOnDevice:
    "Camp cleanup class."

    def __init__(self, lines) -> None:
        self.commands = lines

    def answer(self):
        result = 0
        sizes = []
        for command in self.commands:
            if command.startswith("$"):#this is a command
                if command.startswith("$ cd"):#this is a navigation
                    navTo = command.split()[2]
                    if navTo == "..": #we are going back
                        folderSize = sizes.pop()
                        if folderSize < 100000:
                            result += folderSize
                    elif navTo == "/": #go back to root
                        result += sum([x for x in sizes if x < 100000])
                        sizes.clear()
                    else: #we are going deeper
                        sizes.append(0)
                elif command.startswith("$ ls"):#next lines will be contents
                    pass
                else:
                    raise ValueError("command unknown")
            else: #output of last command
                if command.startswith("dir"):#this is a folder
                    pass
                else:
                    filesize = int(command.split()[0])
                    for i, s in enumerate(sizes):
                        sizes[i] = s + filesize

        return result

if __name__ == '__main__':
    main()
pass


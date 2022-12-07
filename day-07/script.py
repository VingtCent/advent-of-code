"Advent of code day 7."
import re;

def main():
    handle = open(r'./day-07/input', 'r', encoding='UTF8')
    _lines = handle.readlines()
    _impl = NoSpaceLeftOnDevice(_lines)
    print("Answer 1:", _impl.answer1())
    print("Answer 2:", _impl.answer2())


class NoSpaceLeftOnDevice:
    "Camp cleanup class."

    def __init__(self, lines) -> None:
        self.folders = []
        foldersInProgress = []
        for command in lines:
            if command.startswith("$"):#this is a command
                if command.startswith("$ cd"):#this is a navigation
                    navTo = command.split()[2]
                    if navTo == "..": #we are going back
                        folderDone = foldersInProgress.pop()
                        self.folders.append(folderDone)
                    elif navTo == "/": #go back to root
                        if not foldersInProgress:
                            foldersInProgress.append(_Folders(navTo, 0))
                        else:
                            self.folders.extend(foldersInProgress[1:])
                            foldersInProgress[1:] = []
                    else: #we are going deeper
                        foldersInProgress.append(_Folders(navTo, 0))
                elif command.startswith("$ ls"):#next lines will be contents
                    pass
                else:
                    raise ValueError("command unknown")
            else: #output of last command
                if command.startswith("dir"):#this is a folder
                    pass
                else:
                    filesize = int(command.split()[0])
                    for f in foldersInProgress:
                        f.size += filesize
        
        self.folders.extend(foldersInProgress)
        
    def answer1(self):
        return sum([f.size for f in self.folders if f.size <= 100000])

    def answer2(self):        
        for f in self.folders:
            if f.name == "/":
                rootFolderSize = f.size
                break        
        
        freeSpace = 70000000 - rootFolderSize
        if freeSpace < 30000000:
            neededSpace = 30000000 - freeSpace
            folderToDelete = None
            for f in self.folders:
                if f.size >= neededSpace and (not folderToDelete or f.size < folderToDelete.size):
                    folderToDelete = f
            return folderToDelete.size
        
        return None

class _Folders:
    def __init__(self, name:str, size:int) -> None:
        self.name = name
        self.size = size

if __name__ == '__main__':
    main()
pass


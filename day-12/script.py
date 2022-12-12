"Advent of code day 12."

import math


def main():
    "Main."
    handle = open(r"./day-12/input", "r", encoding="UTF8")
    _lines = handle.readlines()
    _impl = HillClimbingAlgorithm(_lines)
    print("Answer 1:", _impl.answer1())
    _impl = HillClimbingAlgorithm(_lines)
    print("Answer 2:", _impl.answer2())


class HillClimbingAlgorithm:
    "Impl class."

    def __init__(self, lines) -> None:
        self.ground = [[p for p in l] for l in lines]
        self.start = self._find("S")[0]
        self.end = self._find("E")[0]

    def _find(self, item):
        matrix = self.ground
        result = []
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == item:
                    result.append((i, j))
        return result

    def answer1(self):
        "Returns answer to part1."
        graph = _Graph()

        def elevation(position):
            return ord(
                position
                if position not in ["S", "E"]
                else ("a" if position == "S" else "z")
            )

        for i, row in enumerate(self.ground):
            for j, value in enumerate(row):
                for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + move[0] < len(self.ground) and 0 <= j + move[1] < len(
                        row
                    ):
                        target = self.ground[i + move[0]][j + move[1]]
                    else:
                        target = None
                    if target:
                        if (
                            (elevation(value) - 1)
                            <= elevation(target)
                            <= (elevation(value) + 1)
                        ):
                            graph.add_edge((i, j), (i + move[0], j + move[1]))
        return graph.get_distance(self.start, self.end)

    def answer2(self):
        "Returns answer to part 2."
        return None


class _Graph:
    def __init__(self) -> None:
        self.edges = dict()

    def add_edge(self, start, end):
        if start in self.edges.keys():
            self.edges[start].append(end)
        else:
            self.edges[start] = [end]

    def get_distance(self, start, end):
        vertices = dict([(k, math.inf) for k in self.edges.keys()])
        vertices[start] = 0

        while vertices:
            current = min(vertices, key=vertices.get)
            if current == end:
                return vertices[current]
            for neighbor in self.edges[current]:
                if neighbor in vertices:
                    vertices[neighbor] = min(vertices[neighbor], vertices[current] + 1)
            vertices.pop(current)


if __name__ == "__main__":
    main()

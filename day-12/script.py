"Advent of code day 12."

import math
from dijkstra import Graph, DijkstraSPF


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

    def __init__(self, lines: list[str]) -> None:
        self._ground = [l.strip() for l in lines]
        self._start = self._find("S")[0]
        self._end = self._find("E")[0]
        self._graph = Graph()

        def elevation(position):
            return ord(
                position
                if position not in ["S", "E"]
                else ("a" if position == "S" else "z")
            )

        for i, row in enumerate(self._ground):
            for j, value in enumerate(row):
                for move in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= move[0] < len(self._ground) and 0 <= move[1] < len(row):
                        target = self._ground[move[0]][move[1]]
                        if elevation(target) <= elevation(value) + 1:
                            self._graph.add_edge((i, j), move, 1)

    def _find(self, item):
        matrix = self._ground
        result = []
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == item:
                    result.append((i, j))
        return result

    def answer1(self):
        "Returns answer to part1."
        dijkstra = DijkstraSPF(self._graph, self._start)
        return dijkstra.get_distance(self._end)

    def answer2(self):
        "Returns answer to part 2."
        closest_start = math.inf
        for i, row in enumerate(self._ground):
            for j, value in enumerate(row):
                if value in ["a", "S"]:
                    dijkstra = DijkstraSPF(self._graph, (i, j))
                    closest_start = min(closest_start, dijkstra.get_distance(self._end))
        return closest_start


if __name__ == "__main__":
    main()

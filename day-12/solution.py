import string
from collections import deque

CHAR_SCORE_MAP = {c: i for i, c in enumerate(string.ascii_lowercase)}

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_start_position(grid: list[str]):
    for row_idx, l in enumerate(grid):
        for col_idx, c in enumerate(l):
            if c == "S":
                return (row_idx, col_idx)


def can_move(grid, dest_row_idx, dest_col_idx, current_value):
    if (
        dest_row_idx < 0
        or dest_col_idx < 0
        or dest_row_idx >= len(grid)
        or dest_col_idx >= len(grid[0])
    ):
        return False

    if current_value == "S":
        current_value = "a"

    dest_value = grid[dest_row_idx][dest_col_idx]

    if dest_value == "E":
        dest_value = "z"

    return CHAR_SCORE_MAP[dest_value] <= CHAR_SCORE_MAP[current_value] + 1


def find_all_low_positions(grid: list[str]):
    for row_idx, l in enumerate(grid):
        for col_idx, c in enumerate(l):
            if c == "S" or c == "a":
                yield (row_idx, col_idx)


def find_shortest_path(grid: list[str], start_positions: list[tuple[int, int]]):
    queue: deque[tuple[tuple[int, int], int]] = deque((p, 0) for p in start_positions)
    seen: set[tuple[int, int]] = set(start_positions)

    while queue:
        (current_row, current_col), current_step_count = queue.popleft()

        current_value = grid[current_row][current_col]

        if current_value == "E":
            print(current_step_count)
            return

        for offset_row, offset_col in MOVES:
            new_coord = (current_row + offset_row, current_col + offset_col)

            if new_coord not in seen and can_move(
                grid, new_coord[0], new_coord[1], current_value
            ):
                seen.add(new_coord)
                queue.append((new_coord, current_step_count + 1))

    print("No path to destination")


def part_one(grid: list[str]):
    start_positions = [find_start_position(grid)]
    find_shortest_path(grid, start_positions)


def part_two(grid: list[str]):
    start_positions = list(find_all_low_positions(grid))
    find_shortest_path(grid, start_positions)


def main():
    with open("day-12/input", "r") as f:
        grid = [l.strip() for l in f.readlines()]

    part_one(grid)
    part_two(grid)


if __name__ == "__main__":
    main()
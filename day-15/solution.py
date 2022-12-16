data = open("day-15/input")
sensors = (
    (
        int(line.split(" ")[2].split("=")[1].strip(",")),
        int(line.split(" ")[3].split("=")[1].strip(":")),
        int(line.split(" ")[8].split("=")[1].strip(",")),
        int(line.split(" ")[9].split("=")[1].strip(",")),
    )
    for line in data.readlines()
)
sensor_dist = ((x, y, (abs(x - xb) + abs(y - yb))) for x, y, xb, yb in sensors)

squares = []
for x, y, d in sensor_dist:
    rx = x + d
    lx = x - d
    ru = rx - y
    rv = rx + y
    lu = lx - y
    lv = lx + y
    squares.append((ru, rv, lu, lv))

u_vals = set(ru for ru, rv, lu, rv in squares) | set(lu for ru, rv, lu, rv in squares)

to_add = set()

for u_val in u_vals:
    to_add.add(u_val + 1)
    to_add.add(u_val - 1)

u_vals |= to_add

u_vals = sorted(u_vals)

u_ranges = {key: [] for key in u_vals}
for index, (ru, rv, lu, lv) in enumerate(squares):
    for u_k in u_vals:
        if ru > lu:
            if lu <= u_k <= ru:
                u_ranges[u_k].append(index)
        else:
            if ru <= u_k <= ru:
                u_ranges[u_k].append(index)

v_ranges = {}

for u, sqs in u_ranges.items():
    ranges = []
    for sq in sqs:
        ru, rv, lu, lv = squares[sq]
        if rv > lv:
            rng = [lv, rv]
        else:
            rng = [rv, lv]
        ranges.append(rng)
    ranges.sort()
    stack = []
    if len(ranges) > 0:
        stack.append(ranges[0])
        for r in ranges[1:]:
            if stack[-1][0] <= r[0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], r[1])
            else:
                stack.append(r)
    v_ranges[u] = stack

for u, v_range in v_ranges.items():
    if len(v_range) == 2:
        v = v_range[0][1] + 1
        x = int(u / 2 + v / 2)
        y = int(v / 2 - u / 2)
        print(x * 4000000 + y)
        break

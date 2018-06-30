r, c = map(int, input().split())

map = []
for i in range(r):
    map.append(input())

g_sheeps = 0
g_wolves = 0

seen = []
for i in range(r):
    for j in range(c):
        initial = [i, j]
        if initial in seen or map[i][j] == '#':
            continue

        frontier = [initial]

        sheeps = 0
        wolves = 0

        while len(frontier):
            coords = frontier.pop()
            x = coords[0]
            y = coords[1]

            if coords not in seen and map[x][y] != '#':
                field = map[x][y]

                if field == 'k':
                    sheeps += 1
                elif field == 'v':
                    wolves += 1

                if x - 1 >= 0:
                    if map[x - 1][y] != '#':
                        frontier.append([x - 1, y])
                if y - 1 >= 0:
                    if map[x][y - 1] != '#':
                        frontier.append([x, y - 1])
                if x + 1 < len(map):
                    if map[x + 1][y] != '#':
                        frontier.append([x + 1, y])
                if y + 1 < len(map[0]):
                    if map[x][y + 1] != '#':
                        frontier.append([x, y + 1])

                seen.append(coords)

        if sheeps > wolves:
            g_sheeps += sheeps
        else:
            g_wolves += wolves

print(g_sheeps, g_wolves)

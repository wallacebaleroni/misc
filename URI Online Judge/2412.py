import math


def dist(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


n, d = map(int, input().split())

coords = []

for i in range(n):
    x, y = map(int, input().split())
    coords.append([x, y])

reachable = [coords[0]]

for i in reachable:
    for j in range(len(coords)):
        if i == coords[j]:
            continue
        dc = dist(i[0], i[1], coords[j][0], coords[j][1])
        if dc <= d:
            reachable.append(coords[j])

if len(reachable) < n:
    print("N")
else:
    print("S")

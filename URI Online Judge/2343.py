n = int(input())

coords = set({})
resp = False

for i in range(n):
    x, y = map(int, input().split())

    if not resp:
        if (x, y) in coords:
            resp = True
        else:
            coords.add((x, y))

if resp:
    print("1")
else:
    print("0")

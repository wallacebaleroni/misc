while True:
    n = int(input())
    if n == 0:
        break

    p1 = 0
    p2 = 0
    for i in range(n):
        j1, j2 = map(int, input().split())

        if j1 > j2:
            p1 += 1
        elif j2 > j1:
            p2 += 1

    print(p1, p2)

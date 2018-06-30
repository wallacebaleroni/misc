m, n = map(int, input().split())

mapa = []

for i in range(m):
    mapa.append(input())

costa = 0

for i in range(m):
    for j in range(n):
        if mapa[i][j] == '#':
            if i > 0:
                if mapa[i - 1][j] == '.':
                    costa += 1
                    continue
            else:
                costa += 1
                continue
            if i < m - 1:
                if mapa[i + 1][j] == '.':
                    costa += 1
                    continue
            else:
                costa += 1
                continue
            if j > 0:
                if mapa[i][j - 1] == '.':
                    costa += 1
                    continue
            else:
                costa += 1
                continue
            if j < n - 1:
                if mapa[i][j + 1] == '.':
                    costa += 1
                    continue
            else:
                costa += 1
                continue

print(costa)

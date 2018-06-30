contador = 0

while True:
    contador += 1

    e, l = map(int, input().split())
    if e == l == 0:
        break

    linhas = {}
    for i in range(l):
        x, y = map(int, input().split())

        if x in linhas:
            linhas[x].append(y)
        else:
            linhas[x] = [y]

        if y in linhas:
            linhas[y].append(x)
        else:
            linhas[y] = [x]

    alcancados = 0
    borda = []
    visitados = []
    chaves = list(linhas.keys())
    borda.append(chaves[0])

    while len(borda) > 0:
        atual = borda.pop(0)

        vizinhos = linhas[atual]
        for v in vizinhos:
            if v not in visitados and v not in borda:
                borda.append(v)

        if atual not in visitados:
            alcancados += 1
            visitados.append(atual)

    print("Teste", str(contador))
    print("normal" if alcancados == e else "falha")
    print("")


'''
6 7
1 2
2 3
3 4
4 5
5 6
6 2
1 5
4 3
1 2
4 2
1 4
0 0

'''
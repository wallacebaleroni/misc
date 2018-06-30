inicial, n = map(int, input().split())

operacoes = []

for i in range(n):
    operacao = input().split()
    operacoes.append(operacao)

jogadores = {"D": inicial, "E": inicial, "F": inicial}

for operacao in operacoes:
    if operacao[0] == "C":
        jogadores[operacao[1]] -= int(operacao[2])
    elif operacao[0] == "V":
        jogadores[operacao[1]] += int(operacao[2])
    elif operacao[0] == "A":
        jogadores[operacao[1]] += int(operacao[3])
        jogadores[operacao[2]] -= int(operacao[3])

print(jogadores["D"], jogadores["E"], jogadores["F"])

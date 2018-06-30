n = int(input())

trilhas = []

for i in range(n):
    trilha = input().split()

    subida1 = 0
    subida2 = 0
    for j in range(1, len(trilha) - 1):
        subida = int(trilha[j + 1]) - int(trilha[j])
        if subida > 0:
            subida1 += subida
    for j in range(len(trilha) - 1, 1, -1):
        subida = int(trilha[j - 1]) - int(trilha[j])
        if subida > 0:
            subida2 += subida

    trilhas.append(min(subida1, subida2))

print(trilhas.index(min(trilhas)) + 1)

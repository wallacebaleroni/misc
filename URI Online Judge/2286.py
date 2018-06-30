contador = 0

while True:
    n = int(input())
    if n == 0:
        break

    jogador1_par = input()
    jogador2_impar = input()

    contador += 1
    print("Teste " + str(contador))

    for i in range(n):
        numeros = input()
        numeros = numeros.split(" ")

        resp = int(numeros[0]) + int(numeros[1])

        if resp % 2 == 0:
            print(jogador1_par)
        else:
            print(jogador2_impar)

    print()
counter = 1

while True:
    n = int(input())
    if n == 0:
        break

    password = [[], [], [], [], [], []]
    final = []

    for i in range(n):
        numbers = []
        letters = []

        string = input().split(" ")

        # Take numbers
        for j in range(0, 10, 2):
            numbers.append([int(string[j]), int(string[j + 1])])

        # Take letters
        for j in range(10, 16):
            letters.append(string[j][0])

        for j in range(6):
            password[j] += numbers[ord(letters[j]) - ord('A')]

    for j in range(6):
        for k in range(2):
            if password[j].count(password[j][k]) == n:
                final.append(password[j][k])

    print("Teste " + str(counter))
    for i in range(6):
        print(final[i], end=" ")
    print("\n")
    counter += 1


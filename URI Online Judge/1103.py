while True:
    h1, m1, h2, m2 = map(int, input().split())

    if h1 == m1 == h2 == m2 == 0:
        break

    tempo = (h2 - h1) * 60 + (m2 - m1)

    if h1 * 60 + m1 >= h2 * 60 + m2:
        tempo += 24 * 60

    print(tempo)

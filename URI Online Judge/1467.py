while True:
    try:
        a, b, c = map(int, input().split())
    except EOFError:
        break

    if a != b == c:
        print("A")
    elif b != a == c:
        print("B")
    elif c != a == b:
        print("C")
    else:
        print("*")

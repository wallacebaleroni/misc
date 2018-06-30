a, b, c, d = map(int, input().split())

if (a < b + c and b < a + c and c < a + b) or (a < b + d and b < a + d and d < a + b) or (a < c + d and c < a + d and d < a + c) or (b < c + d and c < b + d and d < b + c):
    print("S")
else:
    print("N")

w, h, d, r = map(int, input().split())

if w*w + h*h + d*d <= 4 * r * r:
    print("S")
else:
    print("N")

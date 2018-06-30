xAi, yAi, xAf, yAf = map(int, input().split())
xBi, yBi, xBf, yBf = map(int, input().split())

if (xBf < xAi or xBi > xAf or yAf < yBi or yBf < yAi or yBi > yAf or xAf < xBi or yAi > yBf or xAi > xBf):
	print(0)
else:
	print(1)

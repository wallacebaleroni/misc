from jar_problem import *

print("Artificial Intelligence Algorithms:")
print("1 - Jar Problem", end="\n")
print("Type the number corresponding to your choice: ", end="")

n = int(input())
print()

if n == 1:
    print("Choose an algorithm:")
    print("1 - Breadth First Search")
    print("2 - Depth First Search")
    print("Type the number corresponding to your choice: ", end="")

    sn = int(input())
    print()

    print("Use Default Values?(Y/N) ", end="")
    ssn = input()

    if sn == 1:
        print()
        print("Breadth First Search:")
        jar_BFS(3, 5, [0, 4])
    elif sn == 2:
        print()
        print("Depth First Search:")
        jar_DFS(3, 5, [0, 4])

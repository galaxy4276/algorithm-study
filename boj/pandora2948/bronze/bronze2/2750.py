from sys import stdin

N = int(stdin.readline().strip())

arr = sorted([int(stdin.readline().strip()) for _ in range(N)])

for i in arr:
    print(i)

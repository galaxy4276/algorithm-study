from sys import stdin

stdin.readline()

arr = list(map(int, stdin.readline().strip().split()))
v = int(stdin.readline().strip())

vFilter = list(filter(lambda x: x == v, arr))

print(len(vFilter))

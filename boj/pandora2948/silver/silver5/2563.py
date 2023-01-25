from sys import stdin

bounds = 0
ranges = []

for _ in range(int(stdin.readline().strip())):
    x, y = list(map(int, stdin.readline().strip().split()))
    bounds += 100
    ranges.append([x, y])

for i in range(len(ranges)):
    for j in range(i, len(ranges)):
        if ranges[i][0] + 10

print(bounds)
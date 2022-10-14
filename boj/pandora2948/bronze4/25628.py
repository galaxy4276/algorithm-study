from sys import stdin

A, B = list(map(int, stdin.readline().strip().split()))

print(min([A // 2, B]))
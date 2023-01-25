from sys import stdin

A, B = list(map(int, stdin.readline().strip().split()))

print((A + B) * (A - B))

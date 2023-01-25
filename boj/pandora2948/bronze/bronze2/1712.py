from sys import stdin

A, B, C = list(map(int, stdin.readline().strip().split()))

if B >= C:
    print(-1)
    exit()

amount = A // (C - B) + 1

print(amount)

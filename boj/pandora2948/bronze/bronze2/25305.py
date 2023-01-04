from sys import stdin

N, k = list(map(int, stdin.readline().strip().split()))

arr = sorted(list(map(int, stdin.readline().strip().split())))

print(arr[-k])
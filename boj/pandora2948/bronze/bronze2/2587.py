from sys import stdin

arr = sorted([int(stdin.readline().strip()) for _ in range(5)])

print(sum(arr) // 5)
print(arr[2])

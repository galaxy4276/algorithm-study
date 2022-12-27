x, y, w, h = list(map(int, input().strip().split()))

print(min(x, y, w-x, h-y))
from sys import stdin

n = int(stdin.readline().strip())
amount = 0

for i in range(n // 5, -1, -1):
    if (n - (5 * i)) % 3 == 0:
        amount = i + (n - (5 * i)) // 3
        break


print(amount) if amount != 0 else print(-1)

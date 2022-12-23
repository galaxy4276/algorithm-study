from sys import stdin

N, K = list(map(int, stdin.readline().strip().split()))
amount = 0

coins = list()

for _ in range(N):
    coins.append(int(stdin.readline().strip()))

coins = (list(filter(lambda x: x <= K, reversed(coins))))

for coin in coins:
    if K == 0:
        break

    div = K // coin
    if div >= 1:
        K = K % coin
        amount += div
        continue
    continue

print(amount)

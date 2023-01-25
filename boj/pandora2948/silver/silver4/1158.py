from sys import stdin

n, k = list(map(int, stdin.readline().strip().split()))
ways = list()
q = [i for i in range(1, n + 1)]
index = k - 1

for _ in range(n):
    ways.append(q.pop(index))
    if len(q) == 0:
        break
    index = (index + k - 1) % (len(q))

print('<' + ', '.join(map(str, ways)) + '>')

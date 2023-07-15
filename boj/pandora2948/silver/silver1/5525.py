from sys import stdin

N = int(stdin.readline().strip())

P = 'I' + "OI" * N

M = int(stdin.readline().strip())

S = stdin.readline().strip()

count = 0

for i in range(M - len(P)):
    if S[i: i + 2] != 'IO':
        continue

    if S[i: i + len(P)] == P:
        count += 1

print(count)

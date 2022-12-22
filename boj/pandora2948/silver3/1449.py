from sys import stdin

N, L = map(int, stdin.readline().strip().split())
leaks = sorted(list(map(int, stdin.readline().strip().split())))
amount = 0
isSkip = False

while len(leaks) != 0:
    lenBefore = len(leaks)
    leaks = list(filter(lambda x: leaks[0] + L - 1 < x, leaks))
    if lenBefore - len(leaks) >= 1:
        amount += 1

print(amount)
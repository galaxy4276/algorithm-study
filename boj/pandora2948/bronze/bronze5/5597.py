from sys import stdin

applied = sorted(int(stdin.readline().strip()) for i in range(28))
answer = list()

for i in range(1, 31):
    if i not in applied:
        print(i)

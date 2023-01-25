from sys import stdin

k = int(stdin.readline().strip())

stack = list()

for _ in range(k):
    num = int(stdin.readline().strip())
    if num == 0:
        stack.pop()
        continue

    stack.append(num)

print(sum(stack))
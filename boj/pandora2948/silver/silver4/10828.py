from sys import stdin

n = int(stdin.readline().strip())
stack = list()

for _ in range(n):
    msg = stdin.readline().strip().split()
    cmd = msg[0]
    if len(msg) > 1:
        num = int(msg[1])

        if cmd == 'push':
            stack.append(num)

    if cmd == 'pop':
        print(stack.pop()) if len(stack) != 0 else print(-1)

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        print(1) if len(stack) == 0 else print(0)

    elif cmd == 'top':
        print(stack[-1]) if len(stack) != 0 else print(-1)
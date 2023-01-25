from sys import stdin
from collections import deque
n = int(stdin.readline().strip())
arr = deque(list())

for _ in range(n):
    msg = stdin.readline().strip().split()
    cmd = msg[0]
    if len(msg) > 1:
        num = int(msg[1])

        if cmd == 'push':
            arr.append(num)
            continue
    if cmd == 'pop':
        print(arr.popleft()) if len(arr) != 0 else print(-1)

    elif cmd == 'size':
        print(len(arr))

    elif cmd == 'empty':
        print(1) if len(arr) == 0 else print(0)

    elif cmd == 'front':
        print(arr[0]) if len(arr) != 0 else print(-1)

    elif cmd == 'back':
        print(arr[-1]) if len(arr) != 0 else print(-1)

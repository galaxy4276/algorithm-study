from sys import stdin
from collections import deque

t = int(stdin.readline().strip())

for _ in range(t):
    dq = deque(list(stdin.readline().strip()))
    count = 0
    while len(dq) > 0:
        if count < 0:
            break

        if dq.popleft() == '(':
            count += 1

        else:
            count -= 1

    if count != 0:
        print('NO')

    else:
        print('YES')

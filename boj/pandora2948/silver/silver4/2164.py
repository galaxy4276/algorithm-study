from collections import deque

n = int(input())
dq = deque([i for i in range(1, n + 1)])

while len(dq) != 1:
    dq.popleft()

    if len(dq) == 1:
        break

    dq.append(dq.popleft())

print(dq.popleft())

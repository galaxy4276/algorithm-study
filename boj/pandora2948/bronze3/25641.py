from collections import deque
from sys import stdin

N = int(stdin.readline().strip())

dq = deque(list(stdin.readline().strip()))

while True:
  if dq.count('s') == dq.count('t'):
    break
  dq.popleft()

print(''.join(dq))
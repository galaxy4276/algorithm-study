from collections import deque
from sys import stdin

queue = deque(range(1, int(stdin.readline()) + 1))

# 카드를 버릴 차례인지
isDrop = True

while len(queue) != 1 :
  if isDrop :
    queue.popleft()
    isDrop = False

  else :
    queue.append(queue.popleft())
    isDrop = True

print(queue.popleft())

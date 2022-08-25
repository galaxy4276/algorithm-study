from collections import deque
from sys import stdin

queue = deque(range(1, int(stdin.readline()) + 1))

while len(queue) != 1 :
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())

from sys import stdin

m = int(stdin.readline().strip())
balls = [True, False, False]

for _ in range(m):
    x, y = list(map(lambda a: int(a) - 1, stdin.readline().strip().split()))
    balls[x], balls[y] = balls[y], balls[x]
print(balls.index(True) + 1)

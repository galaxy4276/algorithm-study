from sys import stdin

target = stdin.readline().strip()

N = int(stdin.readline().strip())

friends = list()

for _ in range(N):
  friends.append(stdin.readline().strip())
  
print(friends.count(target))
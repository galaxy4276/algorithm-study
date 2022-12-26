from sys import stdin
N = stdin.readline().strip()

dolls = list(map(int, stdin.readline().strip().split()))

amount = 0

while len(dolls):
  dollModi = list(set(dolls))
  dollModi.sort(reverse = True)
  for i in dollModi:
    dolls.remove(i)
  amount += 1

print(amount)

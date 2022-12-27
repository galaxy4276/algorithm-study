from sys import stdin

N = int(stdin.readline().strip())

commands = [stdin.readline().strip() for _ in range(N)]
charLength = len(commands[0])

result = list()

for i in range(charLength) :
  char = list(commands[0])[i]
  count = 1
  for j in range(1, len(commands)) :
    if char == list(commands[j])[i] :
      count += 1
  if count == N :
    result.append(char)
  else :
    result.append("?")

print("".join(result))
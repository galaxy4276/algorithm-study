from sys import stdin

while True :
  num = stdin.readline().strip()

  if num == '0' :
    break

  num = list(num)

  if ''.join(num) == ''.join(reversed(num)) :
    print("yes")

  else :
    print("no")
from sys import stdin

A, B = list(map(int, stdin.readline().strip().split()))

isAttack = True

while True:
  if isAttack:
    B += A
    isAttack = False
  
  else:
    A += B
    isAttack = True
  
  if A >= 5:
    print('yj')
    break
  elif B >= 5:
    print('yt')
    break

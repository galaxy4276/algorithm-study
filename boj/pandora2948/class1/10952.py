from sys import stdin

while True :
  a, b = list(map(int, stdin.readline().strip().split()))
  
  if a + b == 0 :
    break
  
  print(a + b)
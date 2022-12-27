from sys import stdin
while True :
  try :
    a, b = list(map(lambda ele : int(ele), stdin.readline().strip().split()))
    print(a + b)

  except :
    break

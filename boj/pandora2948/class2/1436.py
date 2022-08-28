N = int(input())

initial = 666

while True :
  if '666' in str(initial) :
    N -= 1
    if N == 0 :
      break

  initial += 1

print(initial)
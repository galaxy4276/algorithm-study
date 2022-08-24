from sys import stdin

for _ in range(int(input())) :
  count = 0
  for char in stdin.readline() :
    if char == "(" :
      count += 1
    
    elif char == ")" :
      count -= 1

      if count < 0 :
        print("NO")
        break

  if count == 0 :
    print("YES")
  
  elif count > 0 :
    print("NO")


# retry

from sys import stdin

for _ in range(int(stdin.readline())) :
  isValid = True
  stack = []
  
  for char in stdin.readline().strip() :
    if char == "(" :
      stack.append(char)

    else :
      if stack:
        stack.pop()
      
      else :
        isValid = False
        break

  if stack:
    isValid = False

  print("YES" if isValid else "NO")
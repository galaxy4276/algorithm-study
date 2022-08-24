length = int(input())
values = []

for i in range(0, length) :
  values.append(input())

for i in range(0, length) :
  count = 0
  for j in values[i] :
    if j == "(" :
      count += 1
    
    elif j == ")" :
      count -= 1

      if count < 0 :
        print("NO")
        break

  if count == 0 :
    print("YES")
  
  elif count > 0 :
    print("NO")

# 수들의 합 5
a = int(input())
str, end = 1,1
count, total = 1,1

while end != a:
  if total< a:
    end +=1
    total += end
  elif total > a:
    total -= str
    str += 1
  else:
    count += 1
    end += 1
    total += end


print(count)
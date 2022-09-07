i = int(input())
list = list(map(int,input().split()))
maximum = max(list)
sum = 0
for j in range(len(list)):
    sum += list[j]/maximum * 100
print(round(sum/i,2))
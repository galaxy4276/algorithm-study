count= int(input())
total = 0
list = list(map(int,input().split()))

for i in list:
    a = 0
    for j in range(1,i+1):
        if i % j == 0:
            a += 1
    if a == 2:
        total += 1
print(total)
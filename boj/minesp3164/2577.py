total = int(input())
total *= int(input())
total *= int(input())

list = list(map(int, str(total)))
flist = [0]*10
for i in range(len(list)):
    flist[list[i]] += 1

for j in range(len(flist)):
    print(flist[j])
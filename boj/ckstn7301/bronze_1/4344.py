from posixpath import split
import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

s = []

for i in a:
    p = i[1:] #i = i[1:]로 하면 i[0]으로 나눌때 오류
    k=0
    for j in p:
        if sum(p)/i[0] < j:
            k+=1
    s.append((k/i[0])*100)

for i in s:
    print(f"{i:.3f}%")
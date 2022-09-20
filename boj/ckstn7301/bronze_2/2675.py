#문자열 반복

import sys

a = int(sys.stdin.readline().rstrip())
c = []

for i in range(a):
    b = sys.stdin.readline().strip()
    c.append(b)

for i in c:
    for j in i[2:]:
        print(int(i[0])*j,end="")
    print()


import sys
#상수
a = sys.stdin.readline().split()

b = int(a[0][::-1]) - int(a[1][::-1])

if  b > 0: #거꾸로 한 두 수 뺴서 양수면 앞, 음수면 뒤
    print(a[0][::-1])
else:
    print(a[1][::-1])
print(a)
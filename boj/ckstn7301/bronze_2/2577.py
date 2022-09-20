import sys

b = 1

for i in range(3):
    a = int(sys.stdin.readline())
    b *= a

b = str(b)

for i in range(10):
    print(b.count(str(i)))

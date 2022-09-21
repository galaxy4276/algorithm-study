import sys
#음계
a = list(map(int, sys.stdin.readline().split()))

b = [i+1 for i in range(8)] 

if a==b:
    print("ascending")
elif a[::-1]==b:
    print("descending")
else:
    print("mixed")
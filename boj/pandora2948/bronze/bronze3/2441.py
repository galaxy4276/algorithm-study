l = int(input())
for i in range(l, 0, -1):
    print(('*' * i).rjust(l, ' '))

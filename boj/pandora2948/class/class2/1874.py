from sys import stdin

N = int(stdin.readline().strip())
target = list(reversed([int(stdin.readline().strip()) for _ in range(N)]))
num = 2
stack = [1]
opr = ['+']

while len(target) != 0:
    try:
        if target[-1] > stack[-1]:
            stack.append(num)
            opr.append('+')
            num += 1

        elif target[-1] == stack[-1]:
            target.pop()
            stack.pop()
            opr.append('-')

        else:
            break

    except IndexError:
        stack.append(num)
        opr.append('+')
        num += 1

if len(target) == 0:
    for i in opr:
        print(i)

else:
    print('NO')

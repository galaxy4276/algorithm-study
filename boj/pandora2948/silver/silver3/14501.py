from sys import stdin

n = int(stdin.readline().strip())

interviews = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]

days = [0 for _ in range(n)]

for i in range(n):
    expense = 0
    for j in range(i + 1, i + interviews[i][0] + 1):
        if i + interviews[i][0] + 1 > n:
            break
        if interviews[j][0] < i + interviews[i][0] and interviews[j][1] > i + interviews[i][1] :
            days[j] = interviews[j][1]

print(days)

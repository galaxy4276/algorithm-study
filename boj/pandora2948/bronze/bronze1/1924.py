from sys import stdin

x, y = list(map(int, stdin.readline().strip().split()))

long_month = [1, 3, 5, 7, 8, 10, 12]
short_month = [4, 6, 9, 11]
even_short_month = [2]
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = y

for i in range(x):
    if i in long_month:
        day += 31
        continue

    if i in short_month:
        day += 30
        continue

    if i in even_short_month:
        day += 28
        continue

print(date[day % 7])

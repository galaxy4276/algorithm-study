n = int(input())

i = 1
time = 0

while n > 0:
    if n < i:
        i = 1
        continue

    n -= i
    i += 1
    time += 1

print(time)

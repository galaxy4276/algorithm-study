n = int(input())

fibo = []

for i in range(n + 1):
    if i == 0:
        fibo.append(0)

    elif i < 2:
        fibo.append(1)

    else:
        fibo.append(fibo[i - 1] + fibo[i - 2])

print(fibo[-1])
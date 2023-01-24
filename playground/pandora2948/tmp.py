fibo = list()


def fibonacci(x):
    for i in range(x):
        if i < 2:
            fibo.append(1)
        else:
            fibo.append(fibo[i - 2] + fibo[i - 1])


fibonacci(5)
print(fibo)

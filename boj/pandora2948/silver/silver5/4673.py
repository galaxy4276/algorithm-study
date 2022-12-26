n = set(range(1, 10001))

sums = set()

for i in range(1, 10001):
    sums.add(sum(map(int, list(str(i)))) + i)

result = sorted(list(n - sums))

for i in result:
    print(i)
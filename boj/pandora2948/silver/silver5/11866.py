n, k = list(map(int, input().strip().split()))

result = list()
q = [i for i in range(1, n + 1)]

index = k - 1
for _ in range(n):
    result.append(q.pop(index))
    if len(q) == 0:
        break
    index = (index + k - 1) % len(q)

print('<' + ', '.join(list(map(str, result))) + '>')

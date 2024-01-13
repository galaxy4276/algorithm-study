# a + b + c = d 인 수를 구하라고 했다 하지만 하나씩 다 뽑으려면 O(n^3) 이 걸리기 때문에
# a + b = d - c 인 점을 이용하여 구하여 본다.
#retry
# set 이용
import sys

input = sys.stdin.readline

n = int(input())
s = set()

arr = list(map(int, input().split()))

result = 0
s.add(arr[0] + arr[0])

for i in range(1, n):
  for j in range(i):
    if arr[i] - arr[j] in s:
      result += 1
      break

  for j in range(i + 1):
    s.add(arr[i] + arr[j])

print(result)
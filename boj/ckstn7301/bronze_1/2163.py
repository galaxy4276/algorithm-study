#초콜릿 자르기
import sys

n,m = map(int, sys.stdin.readline().split())
print((n-1)+n*(m-1))
#N-1개로 먼저 자르면 1xM개의 초콜릿이 N개 남음 이 초콜릿을
#자르려면 각각 m-1번씩 N개를 자르면 되므로
# n-1 + (m-1)*n

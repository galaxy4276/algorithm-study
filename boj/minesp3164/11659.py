#구간 합 구하기 4
import sys
input = sys.stdin.readline

count,count_ans = map(int,input().split())
list = list(map(int,input().split()))
perfix_list = [0]
total = 0
for i in range(count):
  total += list[i]
  perfix_list.append(total)
for i in range(count_ans):
  start,end = map(int,input().split())
  print(perfix_list[end] - perfix_list[start-1])


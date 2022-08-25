from sys import stdin

N = int(input())

scores = list(map(lambda ele : int(ele), stdin.readline().strip().split()))

M = max(scores)

modifyScores = list(map(lambda el : el / M * 100, scores))

print(sum(modifyScores) / N)
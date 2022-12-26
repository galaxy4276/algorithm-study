from sys import stdin

cases = [list(map(int, stdin.readline().strip().split())) for _ in range(int(stdin.readline().strip()))]

for case in cases:
    amount = case[0]
    scores = case[1:]
    avg = sum(scores) // amount
    print("%.3f" %(len(list(filter(lambda x: x > avg, scores))) * 100 / amount) + "%")

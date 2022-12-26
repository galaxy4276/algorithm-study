from sys import stdin

N = stdin.readline().strip()
prv = list(map(int, list(N)))[-1]
temp = str(sum(list(map(int, list(N)))))
count = 0


def run_cycle(combi):
    global temp, prv, count
    prv = combi[-1]
    temp = prv + str(sum(map(int, list(combi))))[-1]
    count += 1


run_cycle(list(N))

while int(temp) != int(N):
    run_cycle(temp)

print(count)
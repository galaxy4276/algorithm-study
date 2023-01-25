from sys import stdin

n = int(stdin.readline().strip())

room_capacities = list(map(int, stdin.readline().strip().split()))

a, b = map(int, stdin.readline().strip().split())

room_capacities = list(map(lambda x: x - a, room_capacities))
supervisions = len(room_capacities)

for room in room_capacities:
    if room > 0:
        supervisions += room // b if room % b == 0 else room // b + 1

print(supervisions)
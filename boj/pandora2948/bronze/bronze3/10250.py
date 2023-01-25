from sys import stdin

for _ in range(int(stdin.readline().strip())):
    H, W, N = list(map(int, stdin.readline().strip().split()))
    if N % H != 0:
        room_floor = N % H
        room_number = N // H + 1

    else:
        room_floor = H
        room_number = N // H

    print(f'{room_floor}{str(room_number).rjust(2, "0")}')

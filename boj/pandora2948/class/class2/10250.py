from sys import stdin


def booking_automate(height, width, customer_number):
    room_x = customer_number // height + 1
    room_y = customer_number % height

    if room_x > width:
        raise Exception('Room is full')

    return str(room_y) + str(room_x).rjust(max([len(str(width)), 2]), '0')


for _ in range(int(stdin.readline().strip())):
    H, W, N = list(map(int, stdin.readline().strip().split()))
    print(booking_automate(H, W, N))

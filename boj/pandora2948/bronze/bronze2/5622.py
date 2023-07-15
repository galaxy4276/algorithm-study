from sys import stdin

target = list(stdin.readline().strip())

time = 0

for char in target:
    if ord(char) <= 79:
        spin = (ord(char) - 65) // 3
        time += (spin + 3)
        continue

    if ord(char) <= 83:
        time += 8
        continue

    if ord(char) <= 86:
        time += 9
        continue

    if ord(char) <= 90:
        time += 10
        continue

print(time)

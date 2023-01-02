from sys import stdin

N = int(stdin.readline().strip())


def count_han(number: int):
    count = 0
    for i in range(1, number + 1):
        nums = list(map(int, list(str(i))))
        if i < 100:
            count += 1
            continue
        if (nums[1] - nums[0]) == (nums[2] - nums[1]):
            count += 1
    return count


print(count_han(N))

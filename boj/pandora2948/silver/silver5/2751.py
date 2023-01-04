from sys import stdin

N = int(stdin.readline().strip())

arr = [int(stdin.readline().strip()) for _ in range(N)]


def merge_sort(src: list):
    if len(src) < 2:
        return src

    mid = len(src) // 2
    low_arr = merge_sort(src[:mid])
    high_arr = merge_sort(src[mid:])

    merged_arr = []
    low = high = 0

    while low < len(low_arr) and high < len(high_arr):
        if low_arr[low] < high_arr[high]:
            merged_arr.append(low_arr[low])
            low += 1
        else:
            merged_arr.append(high_arr[high])
            high += 1
    merged_arr += low_arr[low:]
    merged_arr += high_arr[high:]
    return merged_arr


result = merge_sort(arr)
for item in result:
    print(item)
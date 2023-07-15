from sys import stdin

N = int(stdin.readline().strip())

origin = list(sorted(map(int, stdin.readline().strip().split())))

M = int(stdin.readline().strip())

searchItem = list(map(int, stdin.readline().strip().split()))

for item in searchItem:
    lf, rt = 0, N - 1
    isExist = False

    while lf <= rt:
        mid = sum([lf, rt]) // 2

        if origin[mid] == item:
            isExist = True
            print(1)
            break

        elif origin[mid] < item:
            lf = mid + 1
            continue

        elif origin[mid] > item:
            rt = mid - 1
            continue

    if not isExist:
        print(0)
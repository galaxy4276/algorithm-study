a = int(input())
i = 0
point = 1
count = 0
while i < a:
    sentence = input()
    b = [char for char in sentence]
    for j in range(len(b)):
        if b[j] == "X":
            point = 1
        if b[j] == "O":
            count += point
            point += 1
    print(count)
    point = 1
    count = 0
    i += 1
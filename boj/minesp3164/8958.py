a = int(input())
i = 0
while i < a:
    count,sentence = input().split()
    list = []
    sentence = [char for char in sentence]
    for k in range(len(sentence)):
            for j in range(int(count)):
                list.append(sentence[k])
    print("".join(list))
    i+=1

text = input()

for i in range(0, len(text) // 10 + 1):
    print(text[i * 10: (i + 1) * 10])
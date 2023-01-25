from sys import stdin

result = 0

for _ in range(int(stdin.readline().strip())):
    text = stdin.readline().strip()

    ban = []
    prv = text[0]
    is_group_word = True

    for ch in text:
        if ch in ban:
            is_group_word = False
            break

        if ch != prv:
            ban.append(prv)
            prv = ch

    if is_group_word:
        result += 1

print(result)

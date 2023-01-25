target = int(input())

comb = 1
dept = 1

while target > comb:
    comb += dept * 6
    dept += 1

print(dept)

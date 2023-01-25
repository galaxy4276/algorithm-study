from sys import stdin

target = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = 0

text = stdin.readline().strip()

for char in target:
    result += text.count(char)
    text = text.replace(char, '#')

text = text.replace('#', '')
result += len(text)

print(result)

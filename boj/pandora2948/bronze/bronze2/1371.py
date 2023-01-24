from sys import stdin
from functools import reduce

string = reduce(lambda acc, cur: acc + cur, stdin.readlines(), '').strip().replace(' ', '').replace('\n', '')

counts = dict()

chars = set(string)

for char in chars:
    counts[char] = string.count(char)

print(''.join(sorted(filter(lambda x: counts[x] == max(counts.values()), list(counts.keys())))))

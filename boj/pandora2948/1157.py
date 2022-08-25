word = input().upper()

chars = set(word)

counts = {}

for ch in chars :
  counts[ch] = word.count(ch)

maxNum = max(counts.values())

result = dict(filter(lambda elem : elem[1] == maxNum, counts.items()))

if len(result) != 1 :
  print("?")

else :
  print(result.popitem()[0])
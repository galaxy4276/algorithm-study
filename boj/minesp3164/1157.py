## 단어 공부

sentence = input()
sentence = sentence.upper()
d = dict()
for i in sentence:
    if i in d.keys():
        d[i] = d[i]+1
    else:
        d[str(i)] = 1
        
max_value = max(d.values())

max_keys = [key for key, value in d.items() if value == max_value]
if len(max_keys) >= 2:
    print("?")
else:
    print(''.join(map(str,max_keys)))
import sys

a = sys.stdin.readline().rstrip().upper()

b = [chr(65+i) for i in range(26)]

c = []

for i in b: #각 알파벳들 몇개인지 카운팅
    cnt = 0
    for j in a:
        if i == j:
            cnt+=1
    c.append(cnt)

cnt = 0
index = -1

for i in range(len(c)):
    if c[i] == max(c): #맥스값이 하나면 유일 두개 이상이면 ?찍어야함
        index = i
        cnt+=1

if cnt>=2:
    print("?")
else:
    print(b[index])

# retry

import sys

a = sys.stdin.readline().rstrip().upper()

b = [chr(65+i) for i in range(26)]

c = []
d = []

for i in b:
    c.append(a.count(i))

e = max(c) #최댓값 저장
sum = 0 #중복값 판단
index = 0 #인덱스 저장

for i in range(26): #알파벳 개수만큼
    if c[i] - e + 1 > 0: #모든값 - 최댓값 + 1 = 최댓값인 값에 자리만 1
        sum+=1 #즉, 최댓값일 때 1추가
        index = i #인덱스 이때 저장
    if sum>1: #만약 최댓값 2번 발생시
        print("?") #더 이상 계산 x
        break
else: #braak 없이 잘 수행 했다면 
    print(b[index]) #저장한 인덱스 위치의 값을 b에서 불러옴
import collections
import sys


a : int = int(sys.stdin.readline().rstrip())
b : list = []
for _ in range(a):
    b.append(sys.stdin.readline().rstrip())

# # 마지막 단어 처리 문제셍김
# for i in b: 
#     k : str = i[0] #첫 번쨰 요소의 첫번째 문자
#     cnt : int = 0
#     for j in i: #첫 번째요소 순회
#         if k != j: #연속이 끊기면
#             c.append(cnt) #카운팅 저장
#             cnt = 0 #카운팅 초기화
#             k = j #k에 다음 문자 넣어서 비교 시작
#         cnt += 1

# print(c)

cnt : int = 0 # 그룹 단어의 개수

for i in b:
    c = collections.Counter(i) # 각 알파벳의 개수 저장(순서x)
    word : str = "" #알파벳 순회해서 차례대로 개수만큼 곱해서 단어생성
    alhpa : list = [chr(i+97) for i in range(26)] #한 사이클 마다 알파벳 초기화
    for j in i: #단어 하나 씩 순회
        if j in alhpa: #이미 뽑은 단어가 아니면 
            alhpa.remove(j) #그 단어 일단 삭제(한 사이클 동안)
            word += j*c[j] #개수만큼 이어 붙여서 만든게 만약 원본이랑 다르면
    if word == i:          #그룹 단어가 아니다. 라는 논리로 비교 연산 수행 
        cnt += 1 #그룹 단어 카운팅
print(cnt) #전체 사이클 순회 후 출력
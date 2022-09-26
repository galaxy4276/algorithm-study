# Reverse String

# 내 풀이1
s = s[::-1] #공간 복잡도가 1이라 오류남
#수정
s[:] = s[::-1]

# 내 풀이2
s.reverse()

# 투 포인터 스왑 방식

l, r = 0, len(s)-1 #왼, 오
while l<r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1

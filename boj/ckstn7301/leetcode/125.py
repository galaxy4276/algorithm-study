#주어진 문자열이 팰린드롬인지 확인
#대소문자 구분x
#영문자와 숫자만을 대상

# 내 풀이
# import sys
# class Solution:
#     def isPalindrome(s: str) -> bool:
        
#         b = ""

#         c = [chr(i + 65) for i in range(26)] #알파벳 A-Z
#         d = [str(i) for i in range(10)] #str타입의 0-9


#         for i in s.upper(): #다 대문자로
#             if i in c or i in d: #c or d면
#                 b += i #저장
#         return b[:] == b[::-1] #거꾸로랑 원래랑 비교

#     print(isPalindrome("0P"))

# #리스트 풀이
# import collections
# from curses.ascii import isalnum
# import re
# import sys
# class Solution:
#     def isPalindrome(s: str) -> bool:
        
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
        
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True

# #데큐풀이
# from curses.ascii import isalnum
# import re
# import sys
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
  
        
#         strs = collections.deque()
#         for i in s:
#             if i.isalnum():
#                 strs.append(i.lower())
        
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#         return True

# #슬라이싱
# from curses.ascii import isalnum
# import sys
# class Solution:
#     def isPalindrome(s: str) -> bool:
#         s = s.lower()
                
#         s = re.sub('[^a-z0-9]', '', s)
                
#         return s == s[::-1]
        
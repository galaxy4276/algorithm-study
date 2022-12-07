import collections
import re


class Solution:
    def is_palindrome_convert_to_list(self, s: str) -> bool:
        strs = []
        for c in s:
            if c.isalnum():
                strs.append(c.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def is_palindrome_deque(self, s: str) -> bool:
        deque = collections.deque()
        for c in s:
            if c.isalnum():
                deque.append(c.lower())
        while len(deque) > 1:
            if deque.pop() != deque.popleft():
                return False
        return True

    def is_palindrome_slicing(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        return s == s[::-1]

if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome_slicing('A man, a plan, a canal: Panama'))

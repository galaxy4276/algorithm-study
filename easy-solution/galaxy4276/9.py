class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        palin_str = str(x)
        reversed_palin_str = list(reversed(list(palin_str)))

        for i in range(0, len(palin_str)):
          if palin_str[i] != reversed_palin_str[i]:
            return False
        return True

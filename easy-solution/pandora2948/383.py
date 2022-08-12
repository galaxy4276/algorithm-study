class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        length = len(ransomNote)
        count = 0

        for char in ransomNote :
          tmp = magazine
          magazine = magazine.replace(char, "", 1)

          if tmp != magazine :
            count += 1

        if length == count :
          return True

        else :
          return False
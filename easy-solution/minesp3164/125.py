import re
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        new_string = re.sub(r"[^a-zA-Z0-9]","",s)
        splits = [char for char in new_string]
        backsite = []
        frontsite = []
        i = 0
        d = len(splits) - 1
        while i < d:
            backsite.append(splits[i])
            frontsite.append(splits[d])
            i += 1
            d -= 1
        if len(backsite) == len(frontsite):
            for i in range(len(backsite)):
                if(backsite[i] != frontsite[i]):
                    return False
        else:
            return False
        return True

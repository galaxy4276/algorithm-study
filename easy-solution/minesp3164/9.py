class Solution(object):
    def isPalindrome(self, x):
        if (x < 0):
            return False
        elif (x == 0):
            return True
        else:
            x = str(x)
            straight = [char for char in x]
            straight_length = len(straight)
            reverce = list(range(straight_length))
            for i in range(straight_length):
                straight[i] = int(straight[i])
            for i in range(straight_length):
                reverce[i] = straight[straight_length - 1 - i]
                if straight[i] != reverce[i]: return False
            return True

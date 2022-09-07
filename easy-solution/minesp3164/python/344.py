class Solution(object):
    def reverseString(self, s):
        count = 0
        reverse = len(s) -1
        while count < reverse:
            change = s[count]
            s[count] = s[reverse]
            s[resource] = change
            count+=1
            reverse -=1
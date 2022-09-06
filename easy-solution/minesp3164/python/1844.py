class Solution(object):
    def replaceDigits(self, s):
        list = [char for char in s]
        for i in range(1,len(list),2):
            a = ord(list[i - 1])
            b = int(list[i])
            list[i] = chr(a+b)
        return "".join(list)
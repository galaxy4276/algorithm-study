class Solution(object):
    def toLowerCase(self, s):
        list = [char for char in s]
        for i in range(len(list)):
            a = ord(list[i])
            if 65<=a<=90:
                a += 32
                list[i] = chr(a)
        return "".join(list)
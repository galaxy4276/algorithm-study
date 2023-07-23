# Convert a Number to Hexadecimal

class Solution(object):
    def toHex(self, num):
        if num < 0:
            num+= 2**32
        a = hex(num)
        return a[2:]
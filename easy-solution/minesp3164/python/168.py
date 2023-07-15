class Solution(object):
    def convertToTitle(self, columnNumber):
        sen = ""
        while columnNumber != 0:
            columnNumber , b = divmod(columnNumber,26)
            if b == 0:
                columnNumber -= 1
                b = 26
            sen = chr(b+64) + sen
        return sen
class Solution(object):
    def finalValueAfterOperations(self, operations):
        count = 0
        for i in range(len(operations)):
            s = operations[i]
            if "++"in s:
                count+= 1
            if "--" in s:
                count-= 1
        return count
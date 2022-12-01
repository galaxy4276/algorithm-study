class Solution(object):
    def countOperations(self, num1, num2):
        if num1 == 0 or num2 == 0: return 0
        if num1 == num2: return 1
        count = 1
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
                count += 1
            if num1 < num2:
                num2 -= num1
                count += 1
        return count
class Solution(object):
    def alternateDigitSum(self, n):
        number =list(map(int, str(n)))
        total = 0
        for i in range(len(number)):
            if i % 2==0:
                total += number[i]
            else:
                total -= number[i]
        return total
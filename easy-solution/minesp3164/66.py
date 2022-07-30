class Solution(object):
    def plusOne(self, digits):
        digits = [str(i) for i in digits]
        intdigits = int("".join(digits))
        answer = intdigits + 1
        answerList = list(map(int, str(answer)))
        return answerList
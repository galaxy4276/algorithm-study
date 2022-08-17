class Solution(object):
    def thousandSeparator(self, n):
        n = str(n)[::-1]
        answer = ''
        for i in range(len(n)):
            if i % 3 == 0 and i > 0:
                answer = answer + '.' + n[i]
            else:
                answer = answer + n[i]
        return ''.join(answer)[::-1]
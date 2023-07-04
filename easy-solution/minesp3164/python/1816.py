class Solution(object):
    def truncateSentence(self, s, k):
        list = s.split(" ")
        sen = list[0]
        for i in range(1,k):
            sen += " "+list[i]
        return sen
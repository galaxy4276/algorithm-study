class Solution(object):
    def restoreString(self, s, indices):
        list = [char for char in s]
        answer = range(len(indices))
        for i in range(len(indices)):
            answer[indices[i]] = list[i]
        return "".join(answer)
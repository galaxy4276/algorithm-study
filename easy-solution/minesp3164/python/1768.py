class Solution(object):
    def mergeAlternately(self, word1, word2):
        list1 = [char for char in word1 ]
        list2 = [char for char in word2]
        i = 0
        answerlist = []
        if len(list1) > len(list2):
            while i < len(list2):
                answerlist.append(list1[i])
                answerlist.append(list2[i])
                i += 1
            while i < len(list1):
                answerlist.append(list1[i])
                i+=1
        else:
            while i < len(list1):
                answerlist.append(list1[i])
                answerlist.append(list2[i])
                i += 1
            while i < len(list2):
                answerlist.append(list2)
                i+=1
        return ''.join(answerlist)
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        list1 = ''.join(word1)
        list2 = ''.join(word2)
        if list1 == list2:
            return True
        return False
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

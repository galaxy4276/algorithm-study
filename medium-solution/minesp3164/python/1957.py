from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        count1 = Counter(word1)
        count2 = Counter(word2)

        return set(count1.keys()) == set(count2.keys()) and Counter(count1.values()) == Counter(count2.values())

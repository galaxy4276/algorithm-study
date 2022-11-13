import collections
from copy import deepcopy
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]): # -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        print(anagrams)
        return list(anagrams.values())

if __name__ == '__main__':
    s = Solution()
    result: List[List[str]] = s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)

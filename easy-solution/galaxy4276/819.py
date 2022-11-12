import collections
from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in
                 re.sub('[^\w]',  ' ', paragraph).lower().split()
                 if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common()[0][0]

if __name__ == '__main__':
    solution = Solution()
    result: str = solution.mostCommonWord(
        paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
        banned=["hit"]
    )
    print(result)

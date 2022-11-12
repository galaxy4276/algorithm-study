from typing import List


class Solution:
    def reverse_string_two_pointer(self, s: List[str]) -> None:
        first, last = 0, len(s) - 1
        while first < last:
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1

    def reverse_string_pythonic(self, s: List[str]) -> None:
        s.reverse()

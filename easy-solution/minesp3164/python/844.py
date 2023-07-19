class Solution(object):
    def backspaceCompare(self, s, t):
        def build(S):
            ans = []
            for i in S:
                if i != "#":
                    ans.append(i)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
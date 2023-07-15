class Solution(object):
    def maxSubsequence(self, nums, k):
        ans = []
        max_k = sorted(nums,reverse=True)[:k]
        for i in nums:
            if i in max_k:
                ans.append(i)
                max_k.remove(i)
                if len(max_k) == 0:
                    return ans
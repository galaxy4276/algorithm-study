class Solution(object):
    def longestSubarray(self, nums):
        prev , curr , ans = 0,0,0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                ans = max(ans, curr + prev)
                prev = curr
                curr = 0
        ans = max(ans, prev + curr)

        return ans-1 if ans == len(nums) else ans
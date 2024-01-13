# Decompress Run-Length Encoded List

class Solution(object):
    def decompressRLElist(self, nums):
        answer = []

        for i in range(0, len(nums) ,2):
            for _ in range(nums[i]):
                answer.append(nums[i+1])
        return answer
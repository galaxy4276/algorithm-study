class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        list = []
        for i in nums1:
            if (i not in nums2 and i not in nums3):
                pass
            else:
                list.append(i)
        for i in nums2:
            if (i in nums3):
                list.append(i)

        return set(list)
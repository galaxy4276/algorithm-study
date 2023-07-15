class Solution(object):
    def findDifference(self, nums1, nums2):
        dif_nums1 = []
        dif_nums2 = []
        for i in nums1:
            if i not in nums2:
                dif_nums1.append(i)
        for i in nums2:
            if i not in nums1:
                dif_nums2.append(i)

        return [set(dif_nums1), set(dif_nums2)]
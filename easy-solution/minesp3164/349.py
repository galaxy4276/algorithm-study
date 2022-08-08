class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) > len(set2):
            return set1.intersection(set2)
        else:
            return set2.intersection(set1)
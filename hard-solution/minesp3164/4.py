class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        total = nums1 + nums2
        total.sort()
        if len(total) % 2 != 0:
            return (float(total[len(total) / 2]))
        else:
            sum = total[len(total) / 2] + total[(len(total) / 2) - 1]
            return (float(sum) / float(2))

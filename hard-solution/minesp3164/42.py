class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) -1
        total = 0
        left_max,right_max = height[left], height[right]
        while left < right:
            left_max = max(left_max,height[left])
            right_max = max(right_max,height[right])
            if left_max < right_max:
                total += left_max - height[left]
                left += 1
            else:
                total += right_max - height[right]
                right -= 1
        return total
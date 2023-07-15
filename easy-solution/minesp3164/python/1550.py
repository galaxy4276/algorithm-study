#1 just my solution like brute force
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr)-2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False

#2 low time low beats
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        return "111" in "".join([str(i%2) for i in arr])
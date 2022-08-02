class Solution(object):
    def validMountainArray(self, arr):
        biggestCount = 0
        biggest = 0
        if(len(arr) < 3):
            return False
        for i in range(len(arr)):
            if(arr[i] > biggest):
                biggest = arr[i]
                biggestCount = i
        truth = True
        if(biggestCount == len(arr) - 1): return False
        for j in range(len(arr)-1):
            if(arr[i] == biggest): return False
            if (j < biggestCount):
                if(arr[j] < arr[j + 1]):
                    truth = True
                else: return False
            if (j >= biggestCount):
                if(arr[j] > arr[j + 1] ):
                    truth = True
                else: return False
            return truth


        """
        :type arr: List[int]
        :rtype: bool
        """

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        for i in range(len(arr) - 1, -1, -1) :
            cur = arr[i]
            arr[i] = maxNum
            if maxNum < cur :
                maxNum = cur
        return arr
            
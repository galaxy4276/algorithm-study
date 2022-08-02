class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(i != j):
                    if(arr[j] % 2 == 0):
                        if(arr[j] / 2  == arr[i] ):
                            return True
        return False
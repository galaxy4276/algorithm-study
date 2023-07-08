class Solution(object):
    def kLengthApart(self, nums, k):
        a = 0
        b = 0
        for i in range(len(nums)):
            if(nums[i]==0):
                a+=1
                b+=1
            elif(nums[i]==1):
                if(a < k and i != 0 and b!= 1):
                    return False
                else:
                    b += 1
                    a = 0
        return True
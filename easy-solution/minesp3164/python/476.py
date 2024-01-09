# 476. Number Complement

class Solution(object):
    def findComplement(self, num): 
        if(num == 0): return 1

        ans = 0
        i = 0

        while(num):
            if(num % 2 == 0):
                ans += pow(2, i)
            i+=1 
            num /= 2
        return ans
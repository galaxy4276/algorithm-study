class Solution(object):
    def addDigits(self, num):
        count = num
        while count >= 10:
            count = 0
            list1 = [char for char in (str(num))]
            for i in range(len(list1)):
                count += int(list1[i])
            if count >= 10:
                num = count
        return count
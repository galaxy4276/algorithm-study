class Solution(object):
    def largestGoodInteger(self, num):
        mapped_num = map(str,num)
        max = 0
        a = ""
        for i in range(len(mapped_num)-2):
            if(mapped_num[i] == mapped_num[i+1] == mapped_num[i+2]):
                a = mapped_num[i]+mapped_num[i+1]+mapped_num[i+2]
                triple = int(mapped_num[i]+mapped_num[i+1]+mapped_num[i+2])
                if triple > max:
                    max = triple
        if max == 0 and a == "":
            return ""
        if max == 0:
            return "000"
        return str(max)
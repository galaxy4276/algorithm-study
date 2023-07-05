class Solution(object):
    def getLucky(self, s, k):
        a = list(map(str,s))
        list_b = []
        for i in range(len(a)):
            num = ord(a[i]) - 96
            list_b.append(num)
        total = 0
        i = 0
        while(i < k):
            if i == 0:
                sen = ''.join(str(s) for s in list_b)
                list_b = list(map(int,sen))
            total = sum(list_b)
            if total < 10:
                return total
            list_b = list(map(int,str(total)))
            i+=1
        return total
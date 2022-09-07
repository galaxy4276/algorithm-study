
class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        list  = []
        minimum = sys.maxsize
        for i in range(len(arr) - 1 ):
            minimum = min(minimum,abs(arr[i+1] - arr[i]))
        for i in range(len(arr) - 1):
            if(minimum == abs(arr[i+1] - arr[i])):
                a = [arr[i],arr[i + 1] ]
                list.append(a)
        return list
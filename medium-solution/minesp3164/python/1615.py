from collections import defaultdict


class Solution(object):
    def maximalNetworkRank(self, n, roads):
#        max_a = 0
#        ad = defaultdict(set)
#        for a in roads:
#            ad[a[0]].add(a[1])
#            ad[a[1]].add(a[0])
#            for i in range(n):
#            for j in range(i+1,n):
#            current = len(ad[i]) + len(ad[j])
#                if j in ad[i]:
#                    current -= 1
#                max_a = max(max_a,current)
#        return max_a
        max_a = 0
        v = [0 for  i in range(n)]
        for road in roads:
            v[road[1]] += 1
            v[road[0]] += 1
        for i in range(n):
            for j in range(i+1,n):
                if[i,j] in  roads or [j,i] in roads:
                    max_a = max(max_a, v[i] + v[j] -1)
                else:
                    max_a = max(max_a, v[i] + v[j])
        return max_a


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
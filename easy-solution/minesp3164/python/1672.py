class Solution(object):
    def maximumWealth(self, accounts):
        list = []
        for i in range(len(accounts)):
            list.append(sum(accounts[i]))
        return max(list)
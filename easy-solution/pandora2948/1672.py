class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []

        for a in accounts :
          wealth.append(sum(a))

        richest_customer_wealth = max(wealth)

        return richest_customer_wealth


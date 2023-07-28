# Average Salary Excluding the Minimum and Maximum Salary
class Solution(object):
    def average(self, salary):
        return float(sum(salary) - max(salary) - min(salary))/ (len(salary)-2)
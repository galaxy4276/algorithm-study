class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m*n:
            return []
        return [[original[i * n + j] for j in range(n)] for i in range(m)]


"""
array = [[0 for col in range(11)] for row in range(10)]
col == 행 row == 열
갯수를 만드는것
"""
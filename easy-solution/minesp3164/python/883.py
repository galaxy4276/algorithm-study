#Projection Area of 3D Shapes
class Solution(object):
    def projectionArea(self, grid):
        result = 0

        for i in grid:
            result += max(i)
            for j in i:
                if j != 0:
                    result += 1


        for i in range(len(grid[0])) :
            maximum = 0
            for j in grid:
                if j[i] > maximum:
                    maximum = j[i]
            result += maximum
        return result
# Distribute Candies to People
class Solution(object):
    def distributeCandies(self, candies, num_people):
        total = 0
        i = 1
        index = 0
        a = [0 for i in range(num_people)]
        while total < candies:
            a[index] += i
            total += i
            i += 1
            index += 1
            if index == len(a):
                index = 0

        if total > candies:
            a[index -1] -= total-candies

        return a

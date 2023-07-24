class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start

        d1 = sum(distance[start: destination])
        d2 = sum(distance[:start]) + sum(distance[destination:])

        return min(d1, d2)
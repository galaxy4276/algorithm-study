# Minimum Number of Operations to Convert Time
class Solution(object):
    def convertTime(self, current, correct):
        count = 0
        current_time = list(map(int, current.split(":")))
        current_time = current_time[0] * 60 + current_time[1]
        correct_time = list(map(int, correct.split(":")))
        correct_time = correct_time[0] * 60 + correct_time[1]

        while current_time != correct_time:
            minus = correct_time - current_time
            if minus >= 60:
                current_time += 60
                count += 1
            elif minus >= 15:
                current_time += 15
                count += 1
            elif minus >= 5:
                current_time += 5
                count += 1
            else:
                current_time += 1
                count += 1

        return count
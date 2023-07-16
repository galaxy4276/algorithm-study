# Crawler Log Folder

class Solution(object):
    def minOperations(self, logs):
        stack = []
        for i in logs:
            if ".." in i and stack:
                stack.pop()
            elif "." in i:
                pass
            else:
                stack.append(i)

        return len(stack)
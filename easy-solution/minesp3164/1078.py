class Solution(object):
    def findOcurrences(self, text, first, second):
        textlist = text.split(" ")
        answer = []
        for i in range(len(textlist) - 2):
            if textlist[i] == first:
                if textlist[i + 1] == second:
                    answer.append(textlist[i + 2])
        return answer

        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """

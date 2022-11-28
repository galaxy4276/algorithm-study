class Solution(object):
    def checkIfPangram(self, sentence):
        alpabet = set("abcdefghijklmnopqrstuvwxyz")
        list = set(sentence)
        return alpabet == list
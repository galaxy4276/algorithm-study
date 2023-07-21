class Solution(object):
    def detectCapitalUse(self, word):
        m1, m2, m3 = True, True, True
        # 전부 대문자일때
        for i in word:
            if not i.isupper():
                m1 = False
        if m1:
            return True

        # 전부 소문자일때
        for i in word:
            if not i.islower():
                m2 = False
        if m2:
            return True
            # 첫번째만 대문자일때

        for i in range(len(word)):
            if i != 0 and word[i].isupper():
                m3 = False
        if m3:
            return True

        return False
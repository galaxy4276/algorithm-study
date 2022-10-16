def isValid(self, s):
    for x in range(len(s)//2):
        if s=='': return True
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return s==''
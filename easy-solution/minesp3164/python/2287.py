class Solution(object):
    def rearrangeCharacters(self, s, target):
        maxx = []
        for i in range(len(set(target))):
            t_count = target.count(target[i])
            s_count = s.count(target[i])
            if t_count <= s_count:
                maxx.append(s_count // t_count)
            else:
                return 0
        return min(maxx)
class Solution(object):
  def greatestLetter(self, s):
    s = set(s)
    upper, lower = ord('Z'), ord('z')
    for i in range(26):
      if chr(upper - i) in s and chr(lower - i) in s:
        return chr(upper - i)
    return ''
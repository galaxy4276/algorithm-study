# Remove Trailing Zeros From a String

class Solution(object):
  def removeTrailingZeros(self, num):
    a = len(num) - 1
    while num[a] == '0':
      a -= 1
    return num[:a + 1]
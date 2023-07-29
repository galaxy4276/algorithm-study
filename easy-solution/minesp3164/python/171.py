class Solution(object):
  def titleToNumber(self, columnTitle):
    total = 0
    for i in columnTitle:
      total = total * 26 + ord(i) - 64
    return total

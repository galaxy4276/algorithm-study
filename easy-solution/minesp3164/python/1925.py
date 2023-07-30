# Count Square Sum Triples

class Solution(object):
  def countTriples(self, n):
    count = 0
    for i in range(1, n + 1):
      for j in range(i + 1, n + 1):
        k = i ** 2 + j ** 2
        r = int(k ** 0.5)
        if (r ** 2 == k and r <= n):
          count += 2
    return count
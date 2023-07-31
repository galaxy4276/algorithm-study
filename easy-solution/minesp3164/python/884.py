#Uncommon Words from Two Sentences

class Solution(object):
  def uncommonFromSentences(self, s1, s2):
    count = {}

    for i in s1.split():
      count[i] = count.get(i, 0) + 1
    for i in s2.split():
      count[i] = count.get(i, 0) + 1

    return [word for word in count if count[word] == 1]
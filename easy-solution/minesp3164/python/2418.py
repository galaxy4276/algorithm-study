class Solution(object):
  def sortPeople(self, names, heights):
    d = {}
    for i in range(len(names)):
      d[heights[i]] = names[i]

    answer = []
    while len(d) > 0:
      answer.append(d[max(d.keys())])
      del d[max(d.keys())]
    return answer
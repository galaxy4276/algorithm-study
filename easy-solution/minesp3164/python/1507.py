# Reformat Date

class Solution(object):
  def reformatDate(self, date):
    month = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
             "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    answer = ""
    date_list = date.split()
    if int(date_list[0][:-2]) >= 10:
      answer += "-" + date_list[0][:-2]
    else:
      answer += "-0" + date_list[0][:-2]
    answer = "-" + month[date_list[1]] + answer
    return str(date_list[2]) + answer
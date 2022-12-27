from sys import stdin

for _ in range(int(input())) :
  string = list(stdin.readline().strip())
  streak = 0
  score = 0

  for char in string :
    if char == "O" :
      streak += 1
      score += streak

    else :
      streak = 0
  print(score)


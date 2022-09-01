from sys import stdin

while True :
  string = stdin.readline().strip().lower()
  
  if string == "#" :
    break
  
  vowel = ["a", "e", "i", "o", "u"]
  amount = 0
  for char in vowel :
    amount += string.count(char)
  
  print(amount)

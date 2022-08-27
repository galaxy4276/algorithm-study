from sys import stdin

N, M = list(map(int, input().strip().split()))

board = list()
counts = list()

for _ in range(N) :
  board.append(list(stdin.readline().strip()))

for i in range(N - 7) :
  for j in range(M - 7) :
    whiteStart = 0
    blackStart = 0
    for k in range(i, i + 8) :
      for l in range(j, j + 8) :
        if (k + l) % 2 == 0 :
          if board[k][l] != 'W' :
            whiteStart += 1
          if board[k][l] != 'B' :
            blackStart += 1

        else :
          if board[k][l] != 'W' :
            blackStart += 1
          if board[k][l] != 'B' :
            whiteStart += 1
    counts.append(blackStart)
    counts.append(whiteStart)

print(min(counts))
A, B = map(lambda ele : list(reversed(ele)), input().strip().split())

print(max(int(''.join(A)), int(''.join(B))))
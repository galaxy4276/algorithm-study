import sys

a = sys.stdin.readline().strip()

call = {'ABC':3,'DEF':4,'GHI':5,'JKL':6,
        'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
sum=0

for i in list(call.keys()):
    for j in a:
        if j in i:
            sum+=call[i]
            continue
print(sum)
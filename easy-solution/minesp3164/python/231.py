
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return (n&(n-1)) == 0
"""
비트 연산자로  해결
만약 2의 제곱수라면 이것들의 비트는 1000 0000 0000 과 같이 맨 왼쪽이 1이고 나머지는 0이지만
그것의 -1 은  0111 1111 1111 이 된다 둘이 상극이기 떄문에 &연산자를 한다면 0 이 나오게 된다.
"""
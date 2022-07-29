class Solution:
  def mySqrt(self, x: int) -> int:
    low, high = 1, x
    mid = (low + high) // 2
    mid_square = mid * mid
    while not (mid_square <= x and (mid + 1) * (mid + 1) > x):
      if mid_square > x:
        high = mid
      else:
        low = mid
      mid = (low + high) // 2
      mid_square = mid * mid

    return mid

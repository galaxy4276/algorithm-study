class Solution:
    def numberOfSteps(self, num: int) -> int:
        num_process = num
        steps = 0
        while num_process != 0 :
          if num_process % 2 == 0 :
            num_process //= 2

          else :
            num_process -= 1

          steps += 1

        return steps
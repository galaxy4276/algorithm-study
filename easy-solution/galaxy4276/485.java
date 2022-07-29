/**
 * @example
 * Input: nums = [1,1,0,1,1,1]
 * Output: 3
 */

class MaxConsecutiveOnes {
  public static int findMaxConsecutiveOnes(int[] nums) {
    int consecutiveCount = 0;
    int memo = 0;
    for (int n : nums) {
      if (n == 1) {
        if (consecutiveCount == 0) {
          consecutiveCount++;
          memo++;
          continue;
        }
        if (memo != consecutiveCount) {
          memo++;
        } else {
          consecutiveCount++;
          memo++;
        }
      } else {
        memo = 0;
      }
    }
    return consecutiveCount;
  }

  public static void main(String[] args) {
    int[] nums = { 1,1,1,1,1,1,1,1 };
    int result = MaxConsecutiveOnes.findMaxConsecutiveOnes(nums);
    System.out.println(result);
  }

}

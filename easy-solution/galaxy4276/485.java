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

    // https://leetcode.com/problems/max-consecutive-ones/discuss/96715/Easy-Java-Solution
    public static int findMaxConsecutiveOnesRefactored(int[] nums) {
      int result = 0;
      int count = 0;
  
      for (int i = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
          count++;
          result = Math.max(count, result);
        } else count = 0;
      }
  
      return result;
    }

  public static void main(String[] args) {
    int[] nums = { 1,1,1,1,1,1,1,1 };
    int result = MaxConsecutiveOnes.findMaxConsecutiveOnes(nums);
    System.out.println(result);
  }

}

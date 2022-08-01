import java.util.Arrays;

class Solution {
  public void moveZeroes(int[] nums) {
    int p1 = 0;
    for (int i = 0; i < nums.length; i++)
      if (nums[i] != 0)
        nums[p1++] = nums[i];

    for (int i = p1; i < nums.length; i++)
      nums[i] = 0;
  }
}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 0,1,0,3,12 };
    s.moveZeroes(nums);
    Arrays.stream(nums).forEach(System.out::print);
  }
}

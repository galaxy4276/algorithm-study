import java.util.Arrays;

class Solution {
  public int thirdMax(int[] nums) {
    Arrays.sort(nums);
    int len = nums.length, count = 0;
    if (len == 1) return nums[0];
    if (len == 2) return nums[len - 1];
    for (int i = len - 1; i > 0; i--) {
      if (nums[i - 1] != nums[i]) {
        count++;
        if (count == 2)
          return nums[i - 1];
      }
    }

    return nums[len - 1];
  }
}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 3, 2, 1 };
    int result = s.thirdMax(nums);
    System.out.println("result: " + result);
//    Arrays.stream(result).forEach(System.out::print);
  }
}

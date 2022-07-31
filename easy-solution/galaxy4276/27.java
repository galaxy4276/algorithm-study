import java.util.Arrays;

class Solution {
  public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
      if (nums[j] != val) nums[i++] = nums[j];
    }
    return i;
  }

}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 3, 2, 2, 3 };
    int result = s.removeElement(nums, 3);
    Arrays.stream(nums).forEach(System.out::print);
    System.out.println(result);
  }
}

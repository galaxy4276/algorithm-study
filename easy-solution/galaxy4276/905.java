import java.util.Arrays;

class Solution {
  public int[] sortArrayByParity(int[] nums) {
    int len = nums.length;
    if (len <= 1) return nums;
    int[] temp = new int[len];
    int tempHead = 0;

    for (int n : nums)
      if (n % 2 == 0)
        temp[tempHead++] = n;

    for (int n : nums)
      if (n % 2 == 1)
        temp[tempHead++] = n;


    return temp;
  }
}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 3, 1, 2, 4 };
    int[] result = s.sortArrayByParity(nums);
    Arrays.stream(result).forEach(System.out::print);
  }
}

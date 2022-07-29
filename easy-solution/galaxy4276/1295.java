import java.util.Arrays;

public class FindNumbersWithEvenNumberOfDigits {
  public static int findNumbers(int[] nums) {
    int cnt = 0;
    for (int n : nums) {
      String s = String.valueOf(n);
      if (s.length() % 2 == 0) cnt++;
    }
    return cnt;
  }

  // https://leetcode.com/problems/find-numbers-with-even-number-of-digits/discuss/508511/Java-One-Liner
  public static int findNumbersRefactored(int[] nums) {
    return (int) Arrays.stream(nums).mapToObj(String::valueOf).filter(item -> item.length() % 2 == 0).count();
  }

    public static void main(String[] args) {
    int[] nums = { 12,345,2,6,7896 };
    int result = FindNumbersWithEvenNumberOfDigits.findNumbers(nums);
    System.out.println(result);
  }
}

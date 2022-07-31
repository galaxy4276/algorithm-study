import java.util.Arrays;

class Solution {

  /**
   * Input: arr = [10,2,5,3]
   * Output: true
   * Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
   */
  public boolean checkIfExist(int[] arr) {
    boolean isAllZero = false;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] == 0) isAllZero = true;
      else isAllZero = false;
    }

    if (isAllZero) return true;

    for (int i = 0; i < arr.length; i++)
      for (int j = 0; j < arr.length; j++)
        if (arr[i] == arr[j] * 2 && (arr[i] != 0 && arr[j] != 0)) {
          return true;
        }
    return false;
  }
}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { -2,0,10,-19,4,6,-8 };
    boolean result = s.checkIfExist(nums);
    System.out.println("result: " + result);
  }
}

class Solution {
  public boolean validMountainArray(int[] arr) {
    if (arr.length < 3) return false;
    boolean isDownside = false;
    if (arr[0] > arr[1]) return false;
    for (int i = 1; i < arr.length; ++i) {
      if (arr[i - 1] == arr[i]) return false;
      if (isDownside)
        if (arr[i - 1] <= arr[i]) return false;
      if (arr[i - 1] > arr[i])
        if (!isDownside) isDownside = true;
    }

    if (!isDownside) return false;

    return true;
  }

  // https://leetcode.com/problems/valid-mountain-array/discuss/2358213/JAVA-easy-solution-O(n)
  public boolean validMountainArrayRefactored(int[] arr) { // O(n) (기존 대비 수학적 접근)
    int len = arr.length;
    if (len < 3 || arr[0] >= arr[1] || arr[len - 1] >= arr[len - 2]) return false;
    boolean decrease = false;
    for (int i = 1; i < len; i++) {
      int diff = arr[i] - arr[i - 1];
      if (diff == 0 || (diff > 0 && decrease)) return false;
      if (diff < 0 && !decrease) decrease = true;
    }
    return true;
  }
}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 0,1,2,3,4,5,6,7,8,9 };
    boolean result = s.validMountainArray(nums);
    System.out.println("result: " + result);
  }
}

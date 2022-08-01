import java.util.Arrays;

class Solution {
  public int[] replaceElements(int[] arr) {
    if (arr.length == 1) return new int[]{-1};
    int max = arr[0];
    for (int i = 0; i < arr.length; i++) {
      for (int j = i + 1; j < arr.length; j++) {
        if (max < arr[j])
          max = arr[j];
      }
      arr[i] = max;
      max = 0;
    }

    arr[arr.length - 1] = -1;
    return arr;
  }


  /**
   * @url https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/discuss/2356808/JAVA-CODE
   * 기존 O(n^2) 풀이 대비 O(n)으로 풀이 된다.
   */
  public int[] replaceElementsRefactored(int[] arr) {
    int len = arr.length;
    int max = arr[len - 1], temp = arr[len - 1];
    for (int i = len - 2; i >= 0; i--) {
      if (temp > max) {
        max = temp;
        temp = arr[i];
        arr[i] = max;
      } else {
        temp = arr[i];
        arr[i] = max;
      }
    }

    arr[len - 1] = -1;
    return arr;
  }

}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 17,18,5,4,6,1 };
    int[] result = s.replaceElementsRefactored(nums);
    Arrays.stream(result).forEach(System.out::print);
  }
}

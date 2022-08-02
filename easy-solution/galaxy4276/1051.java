import java.util.Arrays;

class Solution {
  public int heightChecker(int[] heights) {
    int indices = 0;
    int[] sorted = new int[heights.length];
    for (int i = 0; i < heights.length; i++)
      sorted[i] = heights[i];
    Arrays.sort(sorted);
    for (int i = 0; i < heights.length; i++)
      if (sorted[i] != heights[i]) indices++;
    return indices;
  }

  // https://leetcode.com/problems/height-checker/discuss/299216/Java-Sort-1ms-O(nlogn)
  public int heightCheckerRefactored(int[] heights) {
    int[] copy = heights.clone();
    Arrays.sort(copy);
    int count = 0;
    for(int i = 0; i < copy.length; i++){
      if(heights[i]!=copy[i])count++;
    }
    return count;
  }
}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 1,1,4,2,1,3 };
    int result = s.heightChecker(nums);
    System.out.println("result: " + result);
//    Arrays.stream(result).forEach(System.out::print);
  }
}

import java.util.Arrays;

class Solution {

  /**
   Input: nums = [0,0,1,1,1,2,2,3,3,4]
   Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
   Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
   It does not matter what you leave beyond the returned k (hence they are underscores).
   */
  public int removeDuplicates(int[] nums) {
    int cnt = 0, temp = 101;
    for (int i = 0; i < nums.length; i++) {
      if (temp != nums[i]) {
        nums[cnt++] = nums[i];
        temp = nums[i];
      }
    }
    nums = Arrays.copyOf(nums, cnt - 1);
    return cnt;
  }

  /**
   * 기존 풀이 대비 temp 변수를 사용하지 않아도 됨 ( 메모리 확보 )
   */
  public int removeDuplicatesRefactored(int[] nums) {
    int currIndex = 0;
    for (int i = 0; i < nums.length; i++)
      if (nums[i] != nums[currIndex])
        nums[++currIndex] = nums[i];
    return currIndex + 1;
  }

}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = {0,0,1,1,1,2,2,3,3,4};
    int result = s.removeDuplicatesRefactored(nums);
    System.out.println();
    System.out.println("result: " + result);
  }
}

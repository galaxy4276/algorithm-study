import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
  public List<Integer> findDisappearedNumbers(int[] nums) {
    Arrays.sort(nums);
    List<Integer> list = new ArrayList<>();
    HashMap<Integer, Integer> map = new HashMap();
    for (int n : nums)
      map.put(n, n);
    for (int i = 1; i <= nums.length; i++)
      if (!map.containsKey(i))
        list.add(i);

    return list;
  }

  // https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/2368314/java-oror-simple
  public List<Integer> findDisappearedNumbersRefactored(int[] nums) {
    List<Integer> list = new ArrayList();
    int[] temp = new int[nums.length];
    for (int i : nums)
      temp[i - 1]++;
    for (int i = 0; i < nums.length; i++)
      if (temp[i] == 0)
        list.add(i + 1);

    return list;
  }
}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums = { 1, 1 };
    List<Integer> result = s.findDisappearedNumbers(nums);
//    System.out.println("result: " + result);
//    Arrays.stream(result).forEach(System.out::print);
    result.forEach(System.out::print);
  }
}

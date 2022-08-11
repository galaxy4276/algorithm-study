import java.util.*;

class Solution {
  final HashMap<Integer, Integer> map = new HashMap<>();
  public List<Integer> intersection(int[][] nums) {
    var result = new ArrayList<Integer>();
    for (int i = 0; i < nums.length; i++) {
      for (int j = 0; j < nums[i].length; j++) {
        int key = nums[i][j];
        System.out.println("key: " + key);
        map.put(key, map.getOrDefault(key, 0) + 1);
      }
    }

    for (Map.Entry<Integer, Integer> entry : map.entrySet())
      if (entry.getValue() == nums.length)
        result.add(entry.getKey());

    return result.stream().sorted().toList();
  }
}

public class Main {
  public static void main(String[] args) {
    var s = new Solution();
    int[][] nums1 = { {7, 34, 45, 10, 12, 27, 13}, {27, 21, 45, 10, 12, 13} };
    var result = s.intersection(nums1);
    result.forEach(c -> System.out.print(c + ", "));
    System.out.println();
  }
}

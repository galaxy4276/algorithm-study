import java.util.*;

class Solution {
  public int[] intersect(int[] nums1, int[] nums2) {
    var nums1Map = new HashMap<Integer, Integer>();
    var countMap = new HashMap<Integer, Integer>();
    var result = new ArrayList<Integer>();

    for (int i : nums1)
      nums1Map.put(i, nums1Map.getOrDefault(i, 0) + 1);

    for (int i : nums2) {
      if (nums1Map.containsKey(i)) {
        int count = nums1Map.get(i);
        if (count > 0) {
          result.add(i);
          nums1Map.put(i, count - 1);
        }
      }
    }

    return Stream.of(result.toArray(new Integer[result.size()])).mapToInt(Integer::intValue).toArray();
  }
}

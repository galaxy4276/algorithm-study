import java.util.*;

class Solution {
  public int[] intersection(int[] nums1, int[] nums2) {
    var list = new ArrayList<Integer>();
    var set = new HashSet<Integer>();
    for (int i : nums1) list.add(i);
    for (int j : nums2)
      if (list.contains(j))
        set.add(j);
    int[] arr = Stream.of(set.toArray(new Integer[set.size()])).mapToInt(Integer::intValue).toArray();
    return arr;
  }
}

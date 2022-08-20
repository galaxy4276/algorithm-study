class Solution {
  public boolean containsDuplicate(int[] nums) {
    var set = new HashSet<Integer>();
    for (int n : nums)
      if (!set.add(n)) return true;
    return false;
  }
}
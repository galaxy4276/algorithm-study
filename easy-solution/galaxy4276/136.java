class Solution {
  public int singleNumber(int[] nums) {
    if (nums.length == 1) return nums[0];
    var map = new HashMap<Integer, Integer>();
    for (int n : nums)
      map.put(n, map.getOrDefault(n, 0) + 1);
    for (var entry : map.entrySet())
      if (entry.getValue() == 1)
        return entry.getKey();
    return nums[1];
  }

  public int better(int[] nums) {
    int result = 0;
    for (int i = 0; i < nums.length; i++)
      result ^= nums[i];
    return result;
  }
}

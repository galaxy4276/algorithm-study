import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;
import java.util.stream.Stream;

/**
 * @retry 2022-08-08
 * @url https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/339051/Java-or-Sliding-Window-template
 */
class Solution {
  public int lengthOfLongestSubstring(String s) {
    int left = 0, right = 0, maxLength = 0;
    for (var map = new HashMap<Character, Integer>(); right < s.length();) {
      var ch = s.charAt(right);
      if (map.containsKey(ch)) {
        maxLength = Math.max(maxLength, right - left);
        left = Math.max(left, map.get(ch) + 1);
      }
      map.put(ch, right++);
    }
    return Math.max(maxLength, right - left);
  }
}

public class Main {
  public static void main(String[] args) {
    Solution s = new Solution();
    int count = s.lengthOfLongestSubstring("abcabcaa");
    System.out.println("count: " + count);
  }
}

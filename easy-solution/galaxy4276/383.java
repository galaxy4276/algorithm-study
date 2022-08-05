import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * @retry 2022-08-05
 */
class Solution {
  public boolean canConstruct(String ransomNote, String magazine) {
    HashMap<Character, Integer> map = new HashMap<>();

    for (int i = 0; i < magazine.length(); i++) {
      char ch = magazine.charAt(i);
      map.put(ch, map.getOrDefault(ch, 0) + 1);
    }

    for (int i = 0; i < ransomNote.length(); i++) {
      char ch = ransomNote.charAt(i);
      int count = map.getOrDefault(ch, 0);
      if (count == 0) return false;
      else map.put(ch, count - 1);
    }

    return true;
  }
}

public class Main {
  public static void main(String[] args) {
    Solution s = new Solution();
    boolean result = s.canConstruct("aa", "aab");
//    result.stream().forEach(n -> {
//      System.out.print(n + ", ");
//    });
    System.out.println("result: " + result);
  }
}

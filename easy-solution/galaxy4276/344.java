
class Solution {
  public void reverseString(char[] s) {
    int slow = 0, fast = s.length - 1;
    while (slow < fast) {
      System.out.println("slow: " + slow + ", fast: " + fast);
      char temp = s[slow];
      s[slow++] = s[fast];
      s[fast--] = temp;
    }
  }
}
public class Main {
  public static void main(String[] args) {
    char[] input = {'H', 'a', 'n', 'n', 'a', 'h'};
    Solution s = new Solution();
    s.reverseString(input);
    for (char c : input) {
      System.out.print(c + ", ");
    }
  }
}

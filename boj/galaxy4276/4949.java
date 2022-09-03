import java.util.*;
import java.io.*;

class Solution {

  public boolean isBalance(Stack<Character> stack, String str) {
    for (char c : str.toCharArray()) {
      if (c == '[' || c == '(') stack.add(c);
      else if (c == ')') {
        if (stack.isEmpty() || stack.peek() != '(') return false;
        stack.pop();
      } else if (c == ']') {
        if (stack.isEmpty() || stack.peek() != '[') return false;
        stack.pop();
      }
    }
    return stack.isEmpty();
  }

}

public class Main {
  public static void main(String[] args) throws IOException {
    final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    final BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
    final Solution s = new Solution();

    while (true) {
      String readed = br.readLine();
      if (readed.equals(".")) break;
      var stack = new Stack<Character>();
      boolean isBalance = s.isBalance(stack, readed);
      if (isBalance) writer.write("yes\n");
      else writer.write("no\n");
    }

    writer.flush(); writer.close();
  }
}

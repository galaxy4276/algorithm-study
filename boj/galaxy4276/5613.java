import java.util.*;
import java.io.*;


class Solution {

  public boolean isOp(String s) {
    return s.equals("+") || s.equals("-") || s.equals("/") || s.equals("*");
  }

  public int calc(int result, int temp, String op) {
    switch (op) {
      case "+": return result + temp;
      case "-": return result - temp;
      case "/": return result / temp;
      case "*": return result * temp;
      default: return result;
    }
  }

  public int getResult(Queue<String> q) {
    int result = 0;
    int tempNumber = 0;
    while (!q.isEmpty()) {
      String s = q.poll();
      if (isOp(s)) {
        int nextNumber = Integer.parseInt(Objects.requireNonNull(q.poll()));
        result = calc(tempNumber, nextNumber, s);
        tempNumber = result;
      } else {
        tempNumber = Integer.parseInt(s);
      }
    }
    return result;
  }

}

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    Solution s = new Solution();
    Queue<String> q = new LinkedList<>();

    while (true) {
      String line = br.readLine();
      if (line.equals("=")) {
        int result = s.getResult(q);
        bw.write(result + "\n");
        break;
      }
      q.add(line);
    }

    bw.flush(); bw.close();
  }

}

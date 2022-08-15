import java.sql.Array;
import java.util.*;

// retry
// https://leetcode.com/problems/happy-number/solution/

class FloydCycleFindingSolution {
  private int getNext(int n) {
    int total = 0;
    while (n > 0) {
      int d = n % 10;
      n /= 10;
      total += d * d;
    }
    return total;
  }

  public boolean isHappy(int n) {
    int slowRunner = n;
    int fastRunner = getNext(n);
    while (fastRunner != 1 && slowRunner != fastRunner) {
      slowRunner = getNext(slowRunner);
      fastRunner = getNext(getNext(fastRunner));
    }
    return fastRunner == 1;
  }

}

class HashSetSolution {
  private int getNext(int n) {
    int total = 0;
    while (n > 0) {
      int d = n % 10;
      n /= 10;
      total += d * d;
    }
    return total;
  }

  public boolean isHappy(int n) {
    var seen = new HashSet<Integer>();
    while (n != 1 && !seen.contains(n)) {
      seen.add(n);
      n = getNext(n);
    }
    return n == 1;
  }

}

class Solution {
  public boolean isHappy(int n) {
    if (n == 1) return true;
    int result = n;
    while (result != 1) {
      result = Arrays.stream(Integer.toString(result).split(""))
              .mapToInt(Integer::parseInt)
              .map(number -> number * number)
              .sum();
    }
    return true;
  }
}


public class Main {
  public static void main(String[] args) {
    var s = new Solution();
    var result = s.isHappy(19);
    System.out.println("result: " + result);
//    result.forEach(c -> System.out.print(c + ", "));
  }
}

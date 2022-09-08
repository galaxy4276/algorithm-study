import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> result = new ArrayList<>();
    List<Integer> prev = null;
    List<Integer> curr = null;

    for (int i = 0; i < numRows; i++) {
      curr = new ArrayList<>();
      for (int j = 0; j <= i; j++)
        if (j == 0 || j == i)
          curr.add(1);
        else
          curr.add(prev.get(j - 1) + prev.get(j));
      prev = curr;
      result.add(curr);
    }

    return result;
  }

}
    
public class Main {

  public static void main(String[] args) {
    Solution s = new Solution();
    List<List<Integer>> res = s.generate(5);
    System.out.println(res);
  }

}

import java.util.*;

class Solution {
  final HashMap<Integer, Boolean> map = new HashMap<>();
  
  public void match(int[] a, int[] b) {
    for (int n : a)
      map.put(n, true);

    for (int n : b) {
      if (map.containsKey(n))
        System.out.println(1);
      else
        System.out.println(0);
    }
  }

}

class Main {  
  public static void main(String args[]) {
    Solution s = new Solution();
    Scanner sc = new Scanner(System.in);
    int size = sc.nextInt();
    int[] a = new int[size];
    for (int i = 0; i < size; i++)
      a[i] = sc.nextInt();
    size = sc.nextInt();
    int[] b = new int[size];
    for (int i = 0; i < size; i++)
      b[i] = sc.nextInt();

    s.match(a, b);
  } 
}

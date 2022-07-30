import java.util.ArrayList;

public class DuplicateZeros {
  public static void duplicateZeros(int[] arr) {
      boolean isCopied = false;
      for (int i = 0; i < arr.length - 1; i++) {
        if (arr[i] == 0) {
          if (isCopied) {
            isCopied = false;
            continue;
          }
          for (int j = arr.length - 1; j >= i + 1; j--) {
            arr[j] = arr[j - 1];
          }

          arr[i + 1] = 0;
          isCopied = true;
        }
      }
  }

  // https://leetcode.com/problems/duplicate-zeros/discuss/1001832/JAVA-using-ArrayList
  public static void duplicateZerosRefactor(int[] arr) {
    int l1 = arr.length;
    ArrayList<Integer> l = new ArrayList();

    // 모든 원소를 l 에 추가한다.
    for (int i = 0; i < l1; i++)
      l.add(arr[i]);

    int j = 0; // l 에 0이 추가된 횟수 ( arr에 비교하여 계산할 때 추가된 횟수만큼 인덱스를 밀어야하기 때문)
    for (int i = 0; i < l1; i++) {
      if (arr[i] == 0) {
        l.add(i + j, 0); // arr 내용에 0이 있다면, l 에 i + j 에 해당하는 인덱스 항목에 0을 추가한다.
        System.out.println();
        j++;
      }
    }

    for (int i = 0; i < arr.length; i++)
      arr[i] = l.get(i);
  }

  public static void main(String[] args) {
    int[] nums = { 1, 0, 2, 3, 0, 4, 5, 0 };
    DuplicateZeros.duplicateZerosRefactor(nums);
    for (int n : nums)
      System.out.printf("%d, ", n);
  }
}

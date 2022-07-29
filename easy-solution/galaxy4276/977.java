import java.util.Arrays;

public class SquaresofaSortedArray {
  public static int[] sortedSquares(int[] nums) {
    int[] squared = new int[nums.length];
    for (int i = 0; i < nums.length; i++)
      squared[i] = nums[i] * nums[i];
    return Arrays.stream(squared).sorted().toArray();
  }

  public static void main(String[] args) {
    int[] nums = { -4, -1, 0, 3, 10 };
    int[] result = SquaresofaSortedArray.sortedSquares(nums);
    System.out.printf("result: ");
    for (int i : result) {
      System.out.printf("%d, ", i);
    }
  }
}

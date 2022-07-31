import java.util.ArrayList;
import java.util.Arrays;

class Solution {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    ArrayList<Integer> arrayList = new ArrayList();

    int i = 0, j = 0;
    while (i < m || j < n) {
      if (i < m && j < n) {
        if (nums1[i] < nums2[j]) arrayList.add(nums1[i++]);
        else arrayList.add(nums2[j++]);
      } else if (i < m) {
        arrayList.add(nums1[i++]);
      } else if (j < n) {
        arrayList.add(nums2[j++]);
      }

    }

    for (int z = 0; z < arrayList.size(); z++)
      nums1[z] = arrayList.get(z);

  }

  // https://leetcode.com/problems/merge-sorted-array/discuss/2354752/Easy-to-understand-solution-in-Java
  public void mergeRefactored(int[] nums1, int m, int[] nums2, int n) {
    int temp1 = m - 1, temp2 = n - 1, finale = m + n - 1;
    while (temp1 >= 0 && temp2 >= 0)
      nums1[finale--] = (nums1[temp1] > nums2[temp2])
              ? nums1[temp1--] : nums2[temp2--];
    while (temp2 >= 0) nums1[finale--] = nums2[temp2--];
  }

}

public class Application {
  public static void main(String[] args) {
    Solution s = new Solution();
    int[] nums1 = { 1, 2, 3, 0, 0, 0 };
    int[] nums2 = { 2, 5, 6 };

    s.mergeRefactored(nums1, 3, nums2, 3);

    Arrays.stream(nums1).forEach(System.out::print);
  }
}

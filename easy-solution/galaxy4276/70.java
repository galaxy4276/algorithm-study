class Solution {
  public int climbStairs(int n) {
    if (n == 1) return 1;
    if (n == 2) return 2;

    int mid, head, rear;
    mid = 1;
    head = 0;
    rear = 0;
    for (int i = 0; i < n; i++) {
      rear = mid + head;
      head = mid;
      mid = rear;
    }

    return rear;
  }
}

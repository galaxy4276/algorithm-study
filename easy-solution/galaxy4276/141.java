class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
    next = null;
  }
}

class Solution {
  public boolean hasCycle(ListNode head) {
    if (head == null) return false;
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && fast.next != null && fast.next.next != null) {
      fast = fast.next.next;
      slow = slow.next;
      if (fast == slow) return true;
    }
    return false;
  }
}

public class Main {
  public static void main(String[] args) {
    Solution s = new Solution();
    ListNode head = new ListNode(3);
    ListNode two = new ListNode(2);
    head.next = two;
    ListNode third = new ListNode(0);
    two.next = third;
    ListNode fourth = new ListNode(-4);
    third.next = fourth;
    fourth.next = two;
    boolean result = s.hasCycle(head);
    System.out.println("result: " + result);
  }
}

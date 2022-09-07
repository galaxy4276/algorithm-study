import java.io.*;

class Solution {
  public ListNode reverseListByRecursive(ListNode head) {
      if (head == null || head.next == null) return head;
      ListNode resultNode = reverseListByRecursive(head.next);
      head.next.next = head;
      head.next = null;
      System.out.println("result Node: " + resultNode.val);
      return resultNode;
  }

  public ListNode reverseListByIteration(ListNode head) {
    ListNode parent = null;
    while (head != null) {
      ListNode curr = head;
      head = head.next;
      curr.next = parent;
      parent = curr;
    }
    return parent;
  }

}

public class Main {
  public static void main(String[] args) {
    Solution s = new Solution();
    ListNode resultNode = s.reverseListByIteration(new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))));
    while (resultNode != null) {
      System.out.print(resultNode.val + "->");
      resultNode = resultNode.next;
    }
  }

}

import java.util.ArrayList;
import java.util.List;


class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
  /**
   * @TimeComplexity O(N)
   * @SpaceComplexity O(N)
   */
  public ListNode middleNodeO_n(ListNode head) {
    ListNode[] A = new ListNode[100];
    int t = 0;
    while (head != null) {
      A[t++] = head;
      head = head.next;
    }
    return A[t / 2];
  }

  /**
   * @TimeComplexity O(N)
   * @SpaceComplexity O(1)
   */
  public ListNode middleNodeO_one(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }
    return slow;
  }
}

public class Main {
  public static void main(String[] args) {
    Solution s = new Solution();
    ListNode firstNode = new ListNode(1);
    ListNode nodeHead = firstNode;
    for (int i = 2; i < 6; i++) {
      ListNode newNode = new ListNode(i);
      nodeHead.next = newNode;
      nodeHead = newNode;
    }

    ListNode node = s.middleNodeO_one(firstNode);
    while (node != null) {
      System.out.print(node.val + ", ");
      node = node.next;
    }
//    result.stream().forEach(n -> {
//      System.out.print(n + ", ");
//    });
    System.out.println();
  }
}

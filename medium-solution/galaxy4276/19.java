// retry 2022-08-11
class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
  public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode fast = head, slow = head;
    for (int i = 0; i < n; i++) fast = fast.next;
    if (fast == null) return head.next;
    while (fast.next != null) {
      fast = fast.next;
      slow = slow.next;
    }
    slow.next = slow.next.next;
    return head;
  }
}

public class Main {
  public static void main(String[] args) {
    var s = new Solution();
    var inputListNode = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
//    var inputListNode = new ListNode(1, new ListNode(2));
    var ListNode = s.removeNthFromEnd(inputListNode, 2);
    var sb = new StringBuilder();

    while (ListNode != null) {
      if (sb.toString() == "") {
        sb.append(ListNode.val); ListNode = ListNode.next;
      } else {
        sb.append("->").append(ListNode.val); ListNode = ListNode.next;
      }
    }
    System.out.println(sb);
  }
}

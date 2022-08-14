import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

// retry 2022-08-10
class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
    next = null;
  }
}

// https://leetcode.com/problems/linked-list-cycle-ii/discuss/44822/Java-two-pointer-solution.
class Solution {

  public ListNode detectCycleUsingSet(ListNode head) {
    Set<ListNode> set = new HashSet<>();

    while (head != null) {
      if (!set.add(head))
        return head;
      head = head.next;
    }
    return null;
  }

  public ListNode detectCycleUsingFloyd(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;

      if (slow == fast) {
        slow = head;
        while (slow != fast) {
          slow = slow.next;
          fast = fast.next;
        }
        return slow;
      }
    }
  }

    public ListNode detectCycle(ListNode head) {
    if (head == null || head.next == null) return null;
    ListNode slow = head, fast = head;
    do {
      if (fast == null || fast.next == null || fast.next.next == null) return null;
      slow = slow.next;
      fast = fast.next.next;
      System.out.println("[loop] slow val: " + slow.val + ", fast val: " + fast.val);
    } while (slow != fast); // slow 는 주기가 시작되는 부분에서 정지하게 됩니다.
    fast = head; // fast 초기화
    System.out.println("sibal :" + slow.val);
    while (slow != fast) {
      slow = slow.next;
      fast = fast.next;
      System.out.println("sort slow val: " + slow.val + ", sort fast val: " + fast.val);
    }
    System.out.println("last slow val: " + slow.val);
    return slow;
  }
}

public class Main {
  public static void main(String[] args) {
    ListNode exampleNode = new ListNode(3);
    ListNode two = new ListNode(2);
    ListNode three = new ListNode(0);
    ListNode four = new ListNode(-4);
    exampleNode.next = two;
    two.next = three;
    three.next = four;
    four.next = two;
    Solution s = new Solution();
    ListNode node = s.detectCycle(exampleNode);
  }
}
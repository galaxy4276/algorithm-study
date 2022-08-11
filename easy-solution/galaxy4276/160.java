import java.sql.Array;
import java.util.*;

// retry 2022-08-10
class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
    next = null;
  }
}

// https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
class Solution {

  public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    if (headA == null | headB == null) return null;
    ListNode a = headA;
    ListNode b = headB;
    while (a != b) {
      a = a == null ? headB : a.next;
      b = b == null ? headA : b.next;
    }
    return a;
  }
}

public class Main {
  public static void main(String[] args) {
    ListNode aOne = new ListNode(4);
    ListNode aTwo = new ListNode(1);
    ListNode aThree = new ListNode(8);
    ListNode aFour = new ListNode(4);
    ListNode aFive = new ListNode(5);
    aOne.next = aTwo; aTwo.next =aThree; aThree.next = aFour; aFour.next = aFive;

    ListNode bOne = new ListNode(5);
    ListNode bTwo = new ListNode(6);
    ListNode bThree = new ListNode(1);
    ListNode bFour = new ListNode(8);
    ListNode bFive = new ListNode(4);
    ListNode bSix = new ListNode(5);
    bOne.next = bTwo; bTwo.next = bThree; bThree.next = bFour; bFour.next = bFive; bFive.next = bSix;

    Solution s = new Solution();
    ListNode node = s.getIntersectionNode(aOne, bOne);

  }
}

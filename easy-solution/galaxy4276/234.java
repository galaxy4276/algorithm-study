class Solution {
  public boolean isPalindrome(ListNode head) {
    var list = new ArrayList<Integer>();
    if (list.size() == 1) return false;
    ListNode iterNode = head;
    while (iterNode != null) {
      list.add(iterNode.val);
      iterNode = iterNode.next;
    }
    int start = 0, last = list.size() - 1;
    while (start <= last)
      if (list.get(start++) != list.get(last--)) return false;
    return true;
  }

  private ListNode reverse(ListNode head) {
    ListNode prev = null;
    while (head != null) {
      ListNode next = head.next;
      head.next = prev;
      prev = head;
      head = next;
    }
    return prev;
  }

  public boolean discuss(ListNode head) {
    ListNode fast = head, slow = head;
    while (fast != null && fast.next != null && slow != null) {
      slow = slow.next;
      fast = fast.next.next;
    }
    if (fast != null) slow = slow.next;
    slow = reverse(slow);
    fast = head;
    while (slow != null && fast != null) {
      if (slow.val != fast.val) return false;
      slow = slow.next;
      fast = fast.next;
    }
    return true;
  }
}
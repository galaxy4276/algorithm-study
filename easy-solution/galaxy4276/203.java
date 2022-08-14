class Solution {
  public ListNode removeElements(ListNode head, int val) {
    var list = new ArrayList<ListNode>();
    ListNode node = head;
    while (node != null) {
      if (node.val != val)
        list.add(node);
      node = node.next;
    }

    if (list.isEmpty()) return null;
    ListNode prevNode = list.get(0);
    prevNode.next = null;
    ListNode res = prevNode;
    for (int i = 1; i < list.size(); i++) {
      ListNode nodeAtList = list.get(i);
      System.out.println("nodeAtList val: " + nodeAtList.val);
      nodeAtList.next = null;
      prevNode.next = nodeAtList;
      prevNode = nodeAtList;
    }

    return res;
  }

  // https://leetcode.com/problems/remove-linked-list-elements/discuss/986302/Java-or-O(n)-time-or-O(1)-space
  public ListNode removeElementsRefactored(ListNode head, int val) {
    if (head == null || (head.next == null && head.val == val)) return null;
    for (; head != null && head.val == val; head = head.next);
    var curr = head;
    while (curr != null && curr.next != null) {
      if (curr.next.val == val)
        curr.next = curr.next.next;
      else
        curr = curr.next;
    }
    return head;
  }
}

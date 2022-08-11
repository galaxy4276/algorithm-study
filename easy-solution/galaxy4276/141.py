class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    if (head == None): return False
    slow = head
    fast = head
    while fast != None and fast.next != None:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        return True
    return False

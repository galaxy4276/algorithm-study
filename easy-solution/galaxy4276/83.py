class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# TODO: Refactoring
class Solution:
  def deleteDuplicates(self, head):
    dulList = []
    init = head
    if head == None:
      return head
    cur = head.next

    dulList.append(head.val)
    while cur != None:
      if cur.val in dulList:
        if cur.next != None:
          if cur.next.val != cur.val:
            head.next = cur.next
            head = cur
        cur = cur.next
        head.next = None
      else:
        dulList.append(cur.val)
        head = cur
        cur = cur.next

    return init


if __name__ == '__main__':
  s = Solution()
  l = ListNode(1, ListNode(1, ListNode(1)))
  r = s.deleteDuplicates(l)
  print(l)

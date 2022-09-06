# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head:
            slow = head
            fast = head.next
            while (slow != fast):
                if fast or fast.next:
                    slow = slow.next
                    fast = fast.next.next
                else:
                    return False
            return True
        return False

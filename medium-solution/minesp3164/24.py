class Solution(object):
    def swapPairs(self, head):
        if not head : return head
        fast = head.next
        slow = head
        while fast and slow:
            change = slow.val
            slow.val = fast.val
            fast.val = change
            slow = fast.next
            if not slow:
                break
            fast = fast.next.next
        return head
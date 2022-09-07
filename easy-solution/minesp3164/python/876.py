# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# saw solution...
class Solution(object):
    def middleNode(self, head):
        list = [head]
        while(list[-1].next):
            list.append(list[-1].next)
        return list[len(list)/ 2 ]
        """
        :type head: ListNode
        :rtype: ListNode
        """


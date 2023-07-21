# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack_l1 = []
        stack_l2 = []

        while l1:
            stack_l1.append(l1.val)
            l1 = l1.next
        while l2:
            stack_l2.append(l2.val)
            l2 = l2.next

        answer = ListNode()
        ans_sum = 0
        i, j = 0, 0
        while stack_l2 or stack_l1:
            if stack_l2:
                ans_sum += stack_l2.pop()
            if stack_l1:
                ans_sum += stack_l1.pop()
            i, ans_sum = divmod(ans_sum, 10)
            answer.val = ans_sum
            prev = ListNode(i)
            prev.next = answer
            answer = prev
            ans_sum = i
        return answer.next if i == 0 else answer

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        answer = ListNode(0)
        curr = answer
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            if  l1 != None:
                n1 = l1.val
            else:
                n1 = 0
            if l2 != None:
                n2 = l2.val
            else:
                n2 = 0
            sum = n1 + n2 + carry
            carry = sum / 10
            curr.next = ListNode(sum%10)
            curr = curr.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        return answer.next

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast;
        ListNode* slow;

        fast = head;
        slow = head;

        while(n){
            fast = fast->next;
            n--;
        }

        if(fast == NULL){
            head = head->next;
            return head;
        }

        while(fast->next){
            slow = slow->next;
            fast = fast->next;
        }

        if(slow->next && slow->next->next){
            slow->next = slow->next->next;
        } else {
            slow->next = NULL;
        }

        return head;
    }
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fast = head, *slow = head;
        for (int i = 0; i < n; i++) fast = fast->next;
        if (!fast) return head->next;
        while (fast->next) fast = fast->next, slow = slow->next;
        slow->next = slow->next->next;
        return head;
    }
};

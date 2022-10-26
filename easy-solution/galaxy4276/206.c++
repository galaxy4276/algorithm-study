#include <iostream>
#include <bits/stdc++.h>
#include <stack>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode* reverseList(ListNode* head) {
    ListNode *nextNode, *prevNode = nullptr;
    while (head) {
      nextNode = head->next;
      head->next = prevNode;
      prevNode = head;
      head = nextNode;
    }
    return prevNode;
  }
};

int main() {
ios::sync_with_stdio(false);
Solution s = *new Solution();
ListNode *result_node = s.reverseList(
    new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))));
while (result_node != nullptr) {
  cout << result_node->val << " ";
  result_node = result_node->next;
}
}

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
    int pairSum(ListNode* head) {
        ListNode* slow=head,*fast=head;
        ListNode* ptr;
        while(fast && fast->next){
            ptr=slow;
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* curr = slow;
        ListNode* prev = NULL, *next = NULL;
        while (curr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        ptr->next=prev;
        ListNode* q=head;
        int result=INT_MIN;
        while(prev){
            int sum=0;
            sum=prev->val+q->val;
            result=max(result,sum);
            prev=prev->next;
            q=q->next;
        }
        return result;
    }
};


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
        ListNode* temp=new ListNode();
        temp->next=head;

        ListNode* ptr1=temp;
        ListNode* ptr2=temp;

        for(int i=1;i<=n;i++){
             ptr1=ptr1->next;
        }

        while(ptr1->next!=NULL){
            ptr1=ptr1->next;
            ptr2=ptr2->next;
        }

        ListNode* denode=ptr2->next;
        ptr2->next=ptr2->next->next;
        delete(denode);
        
        return temp->next;
    }
};
 

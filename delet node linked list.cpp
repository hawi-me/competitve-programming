
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode *temp = node->next;
        while(temp!=NULL){
            if(temp->next==NULL){
                node->val = temp->val;
                node->next = NULL;
                temp = temp->next;
            }
            else{
                node->val = temp->val;
                node = temp;
            temp= temp->next;
            }
            
        }    
    }
};

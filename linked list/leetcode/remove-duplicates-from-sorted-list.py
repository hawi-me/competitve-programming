# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp= head
        while temp.next:
            if temp.val == temp.next.val:
                nextnex=temp.next.next
                delnode = temp.next
                temp.next=nextnex
            else:
                temp=temp.next
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first=head
        second=head.next
        even=second
        odd=first
        while  second and second.next:
            first.next=first.next.next
            second.next=second.next.next
            first=first.next
            second=second.next
        first.next=even
        return odd
        
            

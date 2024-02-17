# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1=ListNode()
        list2=ListNode()
        right , left = list2 , list1
        while head:
            if head.val < x:
                left.next=head
                left=left.next      
            else:
                right.next=head
                right=right.next
            head=head.next
        left.next= list2.next
        right.next = None
        return list1.next
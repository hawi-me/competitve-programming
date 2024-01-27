# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        index=0
        has_cycle=False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                has_cycle=True
                break
        if has_cycle == False:
            return None
        slow = head
        while slow != fast:
            slow= slow.next
            fast = fast.next
        return slow
        

        
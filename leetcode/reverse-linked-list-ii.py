# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next

        # Reverse the sublist
        cur = pre.next
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        pre.next.next = cur
        pre.next = prev

        return dummy.next

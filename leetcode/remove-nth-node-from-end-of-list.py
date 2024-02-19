# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode()
        temp.next = head

        ptr1 = temp
        ptr2 = temp

        for _ in range(n):
            ptr1 = ptr1.next

        while ptr1.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        denode = ptr2.next
        ptr2.next = ptr2.next.next
        del denode

        return temp.next

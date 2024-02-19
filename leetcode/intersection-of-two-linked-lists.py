# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        check={}
        node1=headA
        node2=headB
        while node1:
            if node1 is not check:
                check[node1] = 1
            node1 = node1.next
        while node2:
            if node2 in check:
                return node2
            node2=node2.next
            

        
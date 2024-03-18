# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur=head
        s=0
        lis=[]
        while cur:
            cur = cur.next
            s+=1
        cur = head
        length , rem = s//k , s % k
        for i in range(k):
            lis.append(cur)
            for j in range(length - 1 + (1 if rem else 0)):
                if not cur:
                    break
                cur = cur.next
            rem -= (1 if rem else 0)
            if cur:
                cur.next , cur = None , cur.next
            
        return lis
            
                

        
                
        


        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #creating a dummy node in front
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head
        
        #updating right dynamically
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
            
        #delete
        left.next = left.next.next
        
        return dummyNode.next

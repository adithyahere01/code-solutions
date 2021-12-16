class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        lnext, rnext = left, right  #pointing to lastnode of left & right
        
        while head:
            if head.val < x:
                lnext.next = head  #appending to left next node
                lnext = lnext.next  #Updating lnext
            else:
                rnext.next = head
                rnext = rnext.next
            head = head.next
        
        lnext.next = right.next  #Connecting Left to Right
        rnext.next = None  #Pointing last node of right to NULL
        return left.next

 def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2=0,0
        while l1:
                s1=s1*10+l1.val
                l1=l1.next
        while l2:
                s2=s2*10+l2.val
                l2=l2.next
                
        sum_ = s1 + s2
        dummylist=dummy=ListNode(0)
        if sum_ == 0:
            return dummy
        
        while sum_>0:
            dummy.next = ListNode(sum_ % 10)
            dummy = dummy.next
            sum_ //= 10
            
        prev = None
        dummy = dummylist.next
        while dummy:
            nxt = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nxt
        return prev

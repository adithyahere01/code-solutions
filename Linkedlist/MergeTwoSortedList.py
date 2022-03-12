 def mergeTwoLists(self, l1, l2 ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        #take the remaining last nodes and insert it in output list.
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
    
        return dummy.next

 def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
              #reset slow to head
                slow = head
                
                #move slow & fast pointer one step
                while slow != fast:
                    slow = slow.next
                    fast = fast.next     
                return slow
        
        return None

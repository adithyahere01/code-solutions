class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        #finding middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next   #middle
        slow.next = None   #pointing middle to Null
        
        #Reversing second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
            
        #Merging Two halfs
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1 #shifting pointers
            second = tmp2

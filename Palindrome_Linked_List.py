class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        #keep going until fast is last node or NULL
        #this loop finds the middle when done
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #Reversing the 2nd half of linkedlist
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        #check palindrome
        #using prev
        left,right = head,prev
        #if right reaches the middle stop executing
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      #assiging from head
        cur = head
     
        #while cur not NULL
        while cur:
            #while curr.next not NULL & valuse are same
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
         
           #once removed update cur 
            cur = cur.next
        return head

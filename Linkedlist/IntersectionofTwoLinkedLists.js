var getIntersectionNode = function(headA, headB) {
    //edge case
    if(!headA || !headB) return null
  
    let a = headA, b = headB
  
    while(a !== b){
        a = a.next
        b = b.next
        
        if(!a && !b) return a  
        //if both pointers to null, there is no insection and a === null
            
        if(!a) a = headB  //when pointer2 finishes its list, it will starts over pointer1
        if(!b) b = headA
    }
    
    return a
};

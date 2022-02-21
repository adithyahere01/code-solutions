#Pop elements from s1 
        #-if greater than top element of s2 -> push to s2
        #- else pop top from s2 and push to s1 -> push to s2
   
#Finally, pop all elements from s2 && push back to s1


def sortStacks(s):
    s2 = []

    while s:
        temp = s.pop()
        while s2 and s2[-1] > temp:
            s.append(s2.pop())
        s2.append(temp)

    while s2:
        s.append(s2.pop())

    return s

s = [9,1,7,4]
print(sortStacks(s))

def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        if len(nums)<3: return res
    
        #looping for index and value
        for i,a in enumerate(nums):
             #don't reuse the same value
            if i>0 and a == nums[i-1]:
                continue
            
            #two pointers
            l,r = i+1, len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:       #if equal to 0, add to result
                    res.append([a, nums[l], nums[r]])
                    #update only one pointer
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res

def productExceptSelf(self, nums: List[int]) -> List[int]:
         #Creating a result array with the length of input arr
         res = [1]*(len(nums)) 
    
         prefix = 1                    #first prefix is 1
         for i in range(len(nums)):
            res[i] = prefix
            #updating prefix by multipling with original array value
            prefix *= nums[i]
      
         postfix = 1
         #looping backwards
         for i in range(len(nums)-1,-1,-1):
            #multiplying with already stored prefix value
            res[i] *= postfix
            postfix *= nums[i]
    
         return res

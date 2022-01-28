 def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) = 1 
           return 1
        
        curr = nums[0]
        maxsofar = nums[0]
        
        for num in nums:
            curr = max(num, curr+num)
            if curr > maxsofar:
                maxsofar = curr
        return maxsofar

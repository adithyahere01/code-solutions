  def twoSum(self, nums, target):
        store = dict()
        
        for i in range(len(nums)):
            sec = target - nums[i]
            
            if sec not in store:
                store[nums[i]]=i
            else:
                return [store[sec],i] 

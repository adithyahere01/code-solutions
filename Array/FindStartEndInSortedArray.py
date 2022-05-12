def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def Index(nums,target,check):
            start = 0
            end = len(nums) - 1
            ans = -1
            
            while start <= end:
                mid = (start + end)//2
                if nums[mid] == target:
                    ans = mid
                    if check == 'start':
                        end = mid - 1
                    else:
                        start = mid + 1
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans
        
        return [Index(nums,target,'start'),Index(nums,target,'end')]

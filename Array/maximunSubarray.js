var maxSubArray = function(nums) {
    let curr = nums[0]
    let global = nums[0]
    
    for(let i=1; i<nums.length; i++){
        curr = Math.max(nums[i], curr+nums[i])
        
        if(curr > global){
            global = curr
        }
    }
    return global
};

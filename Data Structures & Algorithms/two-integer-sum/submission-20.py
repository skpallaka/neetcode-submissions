class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for i in range(len(nums)): # -> indexes of list 
            if target - nums[i] in saved: # 3 in saved
                return[saved[target - nums[i]],i] # [ saved[3],3] [0,3] sp mapping value to key(index)            
            else:
                saved[nums[i]] = i # saved[nums[3]]-> saved[6] = 3 since i is 3 at thios time emaning index 
            

        
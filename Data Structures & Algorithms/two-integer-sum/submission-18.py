class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                return [my_dict[complement],i]
            else:
                my_dict[nums[i]] = i 
        return []


    '''
    3,4,5,6
    complement = 7-3 =4
    else:
        my dict[3] = 0  3 is key 0 is val
7-4 = 3
so in mydict so then returns 0,1
    '''

            
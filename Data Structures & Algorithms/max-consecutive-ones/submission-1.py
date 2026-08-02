class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        check_one = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones+=1 # ones = 2
                check_one = max(check_one, ones)
            else:
                ones = 0
        return check_one

        
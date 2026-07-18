class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(nums): # i=0 j =3
            need = target - j #7-3
            if need in seen:
                return [seen[need],i]
            else:
                seen[j] = i 
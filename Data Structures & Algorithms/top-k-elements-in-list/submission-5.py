class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in range(len(nums)):
            key = nums[n] # key = nums[0] -> key = 1
            if key not in seen:
                seen[key] = []
            seen[key].append(n) #1,0 #2,1 #2,2 #3,3 #3,4 #3,5
            # 1:0 , 2:1,2 3:3,4,5
        return sorted(seen, key=lambda k: len(seen[k]), reverse=True)[:k]

        #sorting is onlogn
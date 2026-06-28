class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Thinking process
        
        my_freq = {}

        for num in nums:
            update_dict = my_freq.get(num,0) + 1
            my_freq[num] = update_dict 
        
        sorted_dict = sorted(my_freq.items(), key = lambda item: -item[1])

        result = [pair[0] for pair in sorted_dict[:k]]
        return result

            #WDIJD created a updatinged dictionary that sets a new num that w ehavent 0
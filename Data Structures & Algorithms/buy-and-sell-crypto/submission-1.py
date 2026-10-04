class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            diff = price - min_price
            if diff > max_profit:
                max_profit = diff 
            if price < min_price:
                min_price = price
        return max_profit 

# prices[1:] thisisslicingcreates a new list from index 1 to end    
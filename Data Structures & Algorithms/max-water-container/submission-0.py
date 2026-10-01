class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0,len(heights)-1
        result = 0
        while left < right: #0<7
            width = right - left # 7
            height = min(heights[left],heights[right])#1
            area = width * height # 7,
            result = max(result,area) #7 
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result


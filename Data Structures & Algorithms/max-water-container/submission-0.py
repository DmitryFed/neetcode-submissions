class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        min_height = 0
        while (l < r): 
            
            if min_height < min(heights[l], heights[r]):
                
                min_height = min(heights[l], heights[r])
            
            if res < (r - l) * min_height:
                
                res = (r - l) * min_height
            
            if heights[l] < heights[r]: 
                l+=1
                
            elif heights[l] > heights[r]: 
                r-=1
                
            else:
                r-=1
                l+=1
                
        return res
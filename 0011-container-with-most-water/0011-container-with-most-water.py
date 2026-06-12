class Solution:
    import math
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        n=len(height)
        left=0
        right=n-1
        while left<right:
            h=min(height[left],height[right])
            width=right-left
            area=h*width
            max_area=max(area,max_area)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area


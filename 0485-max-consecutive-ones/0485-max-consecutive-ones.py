class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        max_count=0
        for right in range(n):
            if nums[right]==1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
        return max(max_count,count)


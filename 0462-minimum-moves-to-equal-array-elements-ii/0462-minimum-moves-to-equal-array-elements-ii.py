class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums=sorted(nums)
        t=nums[len(nums)//2]
        count=0
        for i in range(len(nums)):
            count+=abs(t-nums[i])
        return count
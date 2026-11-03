class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_ele=max(nums)
        count=0
        for i in range(len(nums)):
            count+=max_ele-nums[i]
        return count
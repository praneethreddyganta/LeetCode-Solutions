class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            abs(nums[-1]*nums[-2]*(10**5)),
            abs(nums[0]*nums[1]*(10**5)),
            abs(nums[0]*nums[-1]*(10**5))
        )
        
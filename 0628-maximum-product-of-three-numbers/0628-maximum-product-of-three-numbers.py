class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        #GPT GIVEN
        return max(
            nums[-1]*nums[-2]*nums[-3],
            nums[0]*nums[1]*nums[-1]
        )
        '''
        MY CODE:
        I couldn't get the optimal one bcz nen mari ekkuvaga alochinchina
        largest = float('-inf')
        nums.sort()

        for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            prod = nums[i] * nums[j] * nums[k]
            if prod > largest:
                largest = prod

        return largest
       
        '''


        
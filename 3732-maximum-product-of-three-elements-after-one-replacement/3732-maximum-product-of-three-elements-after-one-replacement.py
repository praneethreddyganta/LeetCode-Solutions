class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        MY Initial Code:Time Complexity=O(nlogn)
        nums.sort()
        return max(
            abs(nums[-1]*nums[-2]*(10**5)),
            abs(nums[0]*nums[1]*(10**5)),
            abs(nums[0]*nums[-1]*(10**5)
        )
        '''
        #Optimised Code:Time Complexity=O(N):Took GPT help as well in syntax correction.
        #Learnt one new thing that pointer will got to elif when if fails 
        l=float('-inf')
        sl=float('-inf')
        s=float('inf')
        ss=float('inf')
        for i in range(len(nums)):
            if nums[i]>l:
                sl=l
                l=nums[i]            
            elif nums[i]>sl:
                sl=nums[i]
            if nums[i]<s:
                ss=s
                s=nums[i]            
            elif nums[i]<ss:
                ss=nums[i]
        return max(
            sl*l*(10**5),
            s*ss*(10**5),
            s*l*(-10**5)
        )
        
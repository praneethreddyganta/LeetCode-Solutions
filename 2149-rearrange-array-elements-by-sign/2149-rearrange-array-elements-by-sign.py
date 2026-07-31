class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #Took GPT Help for optmal solution
        l=[0]*len(nums)
        pos_idx=0
        neg_idx=0
        for i in range(len(nums)):
            if nums[i]>0:
                l[2*pos_idx]=nums[i]
                pos_idx+=1
            else:
                l[2*neg_idx+1]=nums[i]
                neg_idx+=1
        return l

        
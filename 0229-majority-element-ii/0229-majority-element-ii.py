from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''Better but not optimal bcz Space:O(N) where I can do with O(1)
        as well.Time will be O(N)'''
        freq=Counter(nums)
        l=[]
        n=len(nums)
        for num in freq:
            if freq[num]>n//3:
                l.append(num)
        return l
        
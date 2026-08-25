from collections import Counter
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # freq=Counter(nums)
        # temp=k
        # while True:
        #     if temp not in freq:
        #         return temp
        #     else:
        #         temp+=k
        # Idea from Karthik Freq pedthey naku number and dhani frequency osthadhi but nak frequency  avasaram ledhu,just a value  kavali anthey
        s=set(nums)
        temp=k
        while True:
            if temp not in s:
                return temp
            else: 
                temp+=k
        
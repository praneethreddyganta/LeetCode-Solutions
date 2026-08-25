from collections import Counter
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        freq=Counter(nums)
        temp=k
        while True:
            if temp not in freq:
                return temp
            else:
                temp+=k


        
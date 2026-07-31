from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        #I Built Logic but GPT helped to build code(syntax)
        freq=Counter(word)
        count=0
        count1=0
        for val in sorted(freq.values(),reverse=True):
            count+=val*(count1//8+1)
            count1+=1
        return count

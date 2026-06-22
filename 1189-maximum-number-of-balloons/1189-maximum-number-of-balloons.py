class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash={}
        for i in text:
            hash[i]=hash.get(i,0)+1
        b_count=hash.get('b',0)
        a_count=hash.get('a',0)
        l_count=hash.get('l',0)//2
        o_count=hash.get('o',0)//2
        n_count=hash.get('n',0)
        return min(b_count,a_count,l_count,o_count,n_count)
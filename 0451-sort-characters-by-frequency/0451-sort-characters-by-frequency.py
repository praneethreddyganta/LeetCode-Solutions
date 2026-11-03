class Solution:
    def frequencySort(self, s: str) -> str:
        #gpt helped and also strivers 
        # Striver dhi nadhi just characters count cheyadamn lo fiff undhi
        # Nen counter vadina vallu oka array create chesaru anni 26 letters pattadaniki
        # EY lambda ardham chuskovali asal idhi em chesthundho sarigga ardham 
        #TUF lo unn question and e question different....
        freq=Counter(s)
        result=sorted(freq.keys(),key=lambda ch:(-freq[ch],ch))
        ans=""
        for i in result:
            ans=ans+freq[i]*i
        return ans
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ''' sum=0
        temp=n
        while temp >0:
            r=temp%10
            sum+=r
            temp=temp//10
        s=str(n)
        l=[]
        for i in range(len(s)):
            if s[i]!="0":
                l.append(s[i])
        n2=int(''.join(l)) if l else 0
        return n2*sum'''
        #GPT GIVEN MORE OPTIMAL
        #Time:O(logn),Space:O(1)
        digit_sum=0
        temp=n
        place=1
        new_num_sum=0
        while temp>0:
            r=temp%10
            digit_sum+=r
            temp=temp//10
            if r!=0:
                new_num_sum+=place*r
                place=place*10
        return new_num_sum*digit_sum




        
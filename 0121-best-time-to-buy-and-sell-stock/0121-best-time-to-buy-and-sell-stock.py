class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        max_profit=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                sell=prices[j]
                max_profit=max(max_profit,sell-buy)
        return max_prof
        '''
        #gpt given
        max_profit=0
        min_price=prices[0]
        for price in prices:
            min_price=min(price,min_price)
            max_profit=max(max_profit,price-min_price)
        return max_profit


        
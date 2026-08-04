class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        h=0
        m = 0
        while l<len(prices)-1:
            if h>len(prices)-1:
                l+=1
                h=l+1
                continue
            if prices[h]<prices[l]:
                l+=1
            elif prices[h]-prices[l]>m:
                m = prices[h]-prices[l]
            
            h+=1
        return m
            
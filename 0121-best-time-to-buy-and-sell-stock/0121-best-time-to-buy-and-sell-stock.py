class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miniprice = prices[0]
        maxProfit =0
        for price in prices :
            if price < miniprice :
                miniprice=price
            profit=price-miniprice
            if profit>maxProfit:
                maxProfit=profit
        return maxProfit  
            
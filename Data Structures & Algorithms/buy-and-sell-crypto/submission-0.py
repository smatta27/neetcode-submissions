class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #best time to buy and sell stocks 

        #best day to buy the stock and sell it 

        #take the min and the max and the profit is 

        #buy when its super cheap, sell when its higher

        maxP = 0
        minBuy = prices[0]

        for sell in prices: 

            #must buy before sell 
            
            maxP = max(maxP, sell - minBuy)

            minBuy = min(minBuy, sell)

        return maxP





        
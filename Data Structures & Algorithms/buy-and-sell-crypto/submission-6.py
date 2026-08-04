class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        cnt = len(prices)
    
        if not prices or cnt == 1: return 0
        
        best_buy = prices[0]
        
        profit = -1
        
        for i in range(1,cnt):
            
            if prices[i] <= best_buy:
                best_buy = prices[i]
                continue 
            
            profit =  profit if prices[i] - best_buy < profit else prices[i] - best_buy
            
        return profit if profit > 0 else 0
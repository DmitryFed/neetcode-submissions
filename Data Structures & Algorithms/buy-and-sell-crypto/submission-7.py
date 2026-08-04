class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        
        best_buy = prices[0]
        profit = 0  # Изначально профит равен 0
        
        for i in range(1, len(prices)):
            if prices[i] < best_buy:
                best_buy = prices[i]  # Нашли цену выгоднее — обновили точку входа
            else:
                # Если цена выше, проверяем, бьёт ли текущий профит наш рекорд
                profit = max(profit, prices[i] - best_buy)
                
        return profit
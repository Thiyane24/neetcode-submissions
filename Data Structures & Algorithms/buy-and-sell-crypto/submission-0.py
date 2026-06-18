class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float('inf')
        max_ = 0

        for price in prices: 
            if price< min_:
                min_ = price
            elif price - min_ > max_:
               max_ = price - min_

        return max_

sol = Solution()

prices= [10,1,5,6,7,1]

print(sol.maxProfit(prices))


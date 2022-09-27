class Solution:
   def solve(self, prices):
      s = 0
      b = float("-inf")
      for i in range(len(prices)):
         temp = b
         b = max(b, s - prices[i])
         if i:
            s = max(s, temp + prices[i - 1])
      return max(s, b + prices[-1])

ob = Solution()
prices = [7,1,5,3,6,4]
print(ob.solve(prices))

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 
Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

# dynamic programming with @cache decorator
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_set = set(coins)
        coins_sorted = sorted(coins_set, reverse=True)
        
        @cache
        def dp(amount_left) -> int:
            valid_coins = []
            for coin in coins_sorted:
                if coin == amount_left:
                    # just 1 coin enough
                    return 1
                # if coin > amount_left, then coin is invalid so exclude the coin
                elif amount_left - coin > 0:
                    valid_coins.append(coin)

            # if valid_coins empty, then no valid solution             
            if not valid_coins:
                return -1
                        
            valid_next_step = []
            for coin in valid_coins:
                if dp(amount_left - coin) > 0:
                    valid_next_step.append(dp(amount_left - coin))
            
            if not valid_next_step:
                return -1
            else:
                return min(valid_next_step) + 1
        
        if amount == 0:
            return 0
        return dp(amount)
"""
# iterative solution, which is faster and uses less memory:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_set = set(coins)
        coins_sorted = sorted(coins_set, reverse=True)
        
        fewest_coins = [float('inf')] * (amount + 1)
        fewest_coins[0] = 0        
        
        for i in range(amount):
            for coin in coins_sorted:
                # if i + coin > amount, there will be an error since fewest_coins list has (amount + 1) elements
                # fewest_coins list elements were initialized to float('inf') so that any finite solution will replace it
                # the goal is the fewest number of coins, so any lower solution should replace it
                # fewest_coins[i] + 1 represents fewest_coins[i] + 1 additional coin 
                if i + coin <= amount and fewest_coins[i] + 1 < fewest_coins[i + coin]:
                    fewest_coins[i + coin] = fewest_coins[i] + 1

        # if float('inf') then  fewest_coins[amount] was never overwritten so no solution exists
        if fewest_coins[amount] == float('inf'):
            return -1
        else:
            return fewest_coins[amount]

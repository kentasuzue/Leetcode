"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        # solution A iterative alternative to dynamic programming
        stairs = [0] * (n + 1)
        stairs[0] = 1
        for i in range(n + 1):
            if i + 1 <= n:
                stairs[i + 1] += stairs[i]
            if i + 2 <= n:
                stairs[i + 2] += stairs[i]                
        return stairs[n]
        
        # solution B that removes if conditions in solution A 
        stairs = [0] * (n + 3)
        stairs[0] = 1
        for i in range(n + 1):
            stairs[i + 1] += stairs[i]
            stairs[i + 2] += stairs[i]                
        return stairs[n]

        # solution C that stores only 3 integers
        stair0 = 1
        stair1 = 0
        stair2 = 0
        for i in range(n):
            stair1 += stair0
            stair2 += stair0
            # print("a", stair0, stair1, stair2)
            stair0 = stair1
            stair1 = stair2
            stair2 = 0
            # print("b", stair0, stair1, stair2)
        return stair0
        
        # solution D that uses dymamic programming but without Python @cache decorator
        def dp(stairs):
            if ways[stairs] != 0:
                return ways[stairs]
            else:
                ways[stairs] = dp(stairs - 1) + dp(stairs - 2)
                return ways[stairs]
        ways = [0] * (n+1)
        ways[0] = 1
        ways[1] = 1        
        dp(n)
        return ways[n]
        """

       # solution E that uses dynamic programming with Python @cache decorator
        @cache
        def dp(stairs: int):
            if stairs == 0:
                return 1
            if stairs == 1:
                return 1
            return dp(stairs - 1) + dp(stairs - 2)
        return dp(n)

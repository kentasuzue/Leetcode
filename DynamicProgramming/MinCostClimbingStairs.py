"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
class Solution:
    """
    # iterative solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * (len(cost) + 1)
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        for step in range(2, len(cost)):
            minCost[step] = cost[step] + min(minCost[step - 1], minCost[step - 2])
        return min(minCost[len(cost) - 1], minCost[len(cost) - 2])

    # dynamic programming solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(step: int) -> int:
            if step <= 1:
                return cost[step]
            else:
                return cost[step] + min(dp(step - 1), dp(step - 2))
        return min(dp(len(cost) - 1), dp(len(cost) - 2))
    
    # dynamic programming solution without python @cache decorator
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(step: int) -> int:
            if minCost[step] != -1:
                return minCost[step]
            else:
                minCost[step] = cost[step] + min(dp(step - 1), dp(step - 2))
                return minCost[step]
        minCost = [-1] * len(cost) # -1 to indicate never visited, since some step costs are 0
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        return min(dp(len(cost) - 1), dp(len(cost) - 2))
    """
    # iterative solution using minimal memory
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost0 = cost[0]
        minCost1 = cost[1]
        for i in range(2, len(cost)):
            minCost2 = cost[i] + min(minCost0, minCost1)
            minCost0 = minCost1
            minCost1 = minCost2        
        return min(minCost0, minCost1)

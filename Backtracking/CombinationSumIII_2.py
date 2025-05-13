"""
Combination Sum III

Solution
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""

class Solution:
    
    import itertools
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(curr, currSum, nextIntBegin, size):
            
            # print(f"curr={curr} currSum={currSum} nextIntBegin={nextIntBegin} size={size}")
            
            if size == k:
                if currSum == n:
                    answers.append(curr[:]) # curr[:] instead of curr will make a copy
                    # print(curr[:])
                    # print(answers)
                    # print("bingo")
                return
            
            # give up if sum is too large
            if currSum >= n:
                return

            remainingPossibleNumbers = 10 - nextIntBegin
            remainingNumbersToFill = k - size
            
            # give up on curr if not enough numbers left to fill out an answer
            if remainingPossibleNumbers < remainingNumbersToFill:
                return
            
            for nextInt in range(nextIntBegin, 10): # iterate up to 9, the highest number
                curr.append(nextInt)
                currSum += nextInt
                size += 1
                backtrack(curr, currSum, nextInt + 1, size)
                curr.pop()
                currSum -= nextInt
                size -= 1
                
        answers = []

        curr = []
        currSum = 0
        nextIntBegin = 1 # out of 1 through 9 allowed numbers, start with the lowest which is 1
        size = 0 # curr is empty
        backtrack(curr, currSum, nextIntBegin, size)
        
        return answers
        

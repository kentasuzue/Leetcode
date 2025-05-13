"""
Numbers With Same Consecutive Differences

Solution
Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.
Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

Example 1:
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 
Constraints:
2 <= n <= 9
0 <= k <= 9
"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def backtracking(curr, i): # curr is string of digits, i is current length of string
            
            if i == n:
                answers.append(int(curr))
                return

            nextDigits = []
            priorDigit = int(curr[-1])
            if k == 0:
                nextDigits.append(priorDigit)
            else:
                if priorDigit - k >= 0:
                    nextDigits.append(priorDigit - k)
                if priorDigit + k <= 9:
                    nextDigits.append(priorDigit + k)
 
            for nextDigit in nextDigits:
                curr += str(nextDigit)
                backtracking(curr, i + 1)
                curr = curr[:-1]
            
        answers = []

        for i in range(1, 10):
            curr = str(i)
            backtracking(curr,1)
        
        return answers

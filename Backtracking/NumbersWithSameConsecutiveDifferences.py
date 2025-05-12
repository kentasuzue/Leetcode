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

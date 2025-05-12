class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(curr, i): # curr is string of parentheses, i is tuple of left and right parentheses
            
            left_paren, right_paren = i
            
            if left_paren < right_paren:
                return
            
            if left_paren > n:
                return
            
            if (left_paren, right_paren) == (n, n):
                answers.append(curr)
                return
            
            for paren in ("(", ")"):
                if paren == "(":
                    left_paren += 1
                else:
                    right_paren += 1
                
                curr += paren
                backtrack(curr, (left_paren, right_paren))
                
                if paren == "(":
                    left_paren -= 1
                else:
                    right_paren -= 1
                    
                curr = curr[:-1]
                
        answers = []
        backtrack("", (0, 0))
        return answers
        

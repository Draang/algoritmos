
"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. 
Return an integer that represents the value of the expression.
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values=[]
        op={'+':lambda  x,y:x+y,
            '-':lambda  x,y:x-y,
            '*':lambda  x,y:x*y,
            '/':lambda  x,y:x/y}
        for token in tokens:
            if token in op:
                last=values.pop()
                first=values.pop()
                r=op[token](first,last)
                r=int(r)
                values.append(r)
            else:
                v=int(token)
                values.append(v)
        return values.pop()
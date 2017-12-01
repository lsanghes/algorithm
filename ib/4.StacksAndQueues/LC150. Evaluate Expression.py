'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another
expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution:
    # @param A : list of strings
    # @return an integer

    # int() rounds both -ve and +ve numbers towards zero
    # // floor division always rounds towards floor
    def evalRPN(self, A):
        stack = []
        operators = {'+': lambda x,y : x + y,
                     '-': lambda x,y : x - y,
                     '*': lambda x,y : x * y,
                     '/': lambda x,y : int(x/float(y))}
        for a in A:
            if a in operators:
                y = stack.pop()
                x = stack.pop()
                result = operators[a](x, y)
                stack.append(result)
            else:
                stack.append(int(a))
        return stack.pop()

# test
print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = list()
        for ele in tokens:
            if ele.isnumeric() or (ele.startswith('-') and ele[1:].isnumeric()):
                stack.append(int(ele))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if ele == operators[0]:
                    res = int(op1 + op2)
                elif ele == operators[1]:
                    res = int(op1 - op2)
                elif ele == operators[2]:
                    res = int(op1 * op2)
                elif ele == operators[3]:
                    res = int(op1 / op2)
                stack.append(res)
        return stack[-1]
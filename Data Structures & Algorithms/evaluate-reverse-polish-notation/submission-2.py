from collections import deque
import operator
import math
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        
        op = deque()
        ops = { "+": operator.add, "-": operator.sub,
         "*":operator.mul, "/":operator.truediv}
        for t in tokens:
            if t in ops.keys():
                first = op.pop()
                second = op.pop()
                op.append(math.trunc(ops[t](second,first)))
            else:
                op.append(int(t))
        return list(op)[0]


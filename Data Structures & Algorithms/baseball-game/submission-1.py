class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        previous_score = 0
        for operation in operations:

            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                new_score = 2 * stack[-1]
                stack.append(new_score)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        
        return sum(stack)

        
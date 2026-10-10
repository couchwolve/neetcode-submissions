class Solution:
    def calPoints(self, operations: List[str]) -> int:

        ans = []

        for operation in operations:

            if operation == '+':
                ans.append(ans[-1]+ans[-2])
            elif operation == 'D':
                ans.append(2*ans[-1])
            elif operation == 'C':
                ans.pop(-1)
            else:
                ans.append(int(operation))
        return sum(ans)

        
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res = []

        for i in operations:

            if i == "+" :
                res.append(res[-1] + res[-2])
            elif i == "C":
                res.pop()
            elif i == "D":
                popped = res[-1]
                res.append(2 * int(popped))
            else:
                res.append(int(i))

        return sum(res)

        



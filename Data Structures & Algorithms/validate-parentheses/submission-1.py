class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {"]": "[", "}":"{", ")":"("}
        res = []
        for i in s:

            if not res:
                res.append(i)
                continue

            if i in ["[", "{", "("]:
                res.append(i)
            else:
                while res:
                    val = res.pop()
                    if val == brackets[i]:
                        break
                    else:
                        return False
        
        return len(res) == 0
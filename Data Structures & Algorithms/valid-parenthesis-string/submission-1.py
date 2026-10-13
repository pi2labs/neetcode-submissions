class Solution:
    def checkValidString(self, s: str) -> bool:
        mp = {')':'('}

        stack = []
        star_stack = []

        for index, val in enumerate(s):
            
            if val == "(":
                stack.append((index, val))
            elif val == "*":
                star_stack.append((index, val))
            else:
                if stack:
                    k,v = stack[-1]
                    if v == mp[val]:
                        stack.pop()
                elif star_stack:
                    ks, vs = star_stack[-1]
                    if index > ks:
                        star_stack.pop()
                else:
                    return False
                    
        while stack and star_stack:
            k,v = stack[-1]
            ks, vs = star_stack[-1]
            
            if k < ks:
                stack.pop()
                star_stack.pop()
            else:
                break
        return len(stack) == 0
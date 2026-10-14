import json
class Solution:
    def encode(self, strs: List[str]) -> str:
        st = ''

        for v in strs:
            st += "nagarjun" + v
        print(st)
        return st
    
    def decode(self, s: str) -> List[str]:
        s = s.split("nagarjun")
        return s[1:]
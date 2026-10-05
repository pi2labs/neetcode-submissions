class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}
        
        for st in strs:
            alphabets = [0] * 26

            for s in st:
                index = ord(s) - ord('a')
                alphabets[index] += 1
            
            hashed = tuple(alphabets)
            if hashed not in mp:
                mp[hashed] = [st]
            else:
                mp[hashed].append(st)
        
        values = mp.values()
        return list(values)


        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mp = collections.Counter(s)
        t_mp = collections.Counter(t)

        if len(s_mp) != len(t_mp):
            return False

        for k, v in s_mp.items():
            if k not in t_mp:
                return False
            
            if v != t_mp[k]:
                return False
        
        return True
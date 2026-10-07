class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for i in s:
            if i.isalnum():
                new_s += i
            
        
        i = 0
        j = len(new_s) - 1

        while i <= j:
            if new_s[i] != new_s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
        
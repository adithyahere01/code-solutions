class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        
        for c in s:
            d1[c] = 1 + d1.get(c,0)
        
        for i in t:
            if i not in d1:
                return False
            else:
                d1[i] -= 1
                
        for val in d1.values():
            if val != 0: return False
        
        return True

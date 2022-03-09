class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            sortedWord = ''.join(sorted(s))
            
            if sortedWord not in res:
                res[sortedWord] = [s]
            else:
                res[sortedWord].append(s)
                
        final = []
        for val in res.values():
            final.append(val)
            
        return final

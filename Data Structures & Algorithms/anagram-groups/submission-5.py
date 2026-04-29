from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            hist = [0] * 26
            for c in s:
                hist[ord(c)- ord("a")] += 1
            
            map[tuple(hist)].append(s)
        
        return list(map.values())


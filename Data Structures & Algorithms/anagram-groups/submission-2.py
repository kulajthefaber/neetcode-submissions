from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        listt = []
        for i in range(len(strs)):
            one_set = []
            if i not in map:
                one_set.append(strs[i])
                map[i] = strs[i]
            for j in range(i+1, len(strs)):
                if self.getStrHist(strs[i]) == self.getStrHist(strs[j]) and (j not in map):
                    one_set.append(strs[j])
                    map[j] = strs[j]
            if one_set:
                listt.append(one_set)
        return listt        


    def getStrHist(self, strr):
        hist = [0] * 26
        for c in strr:
            i = ord(c) - ord("a")
            hist[i] += 1
        return hist
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.getLetterHist(s) == self.getLetterHist(t)

    def getLetterHist(self, s:str) -> list:
        hist = [0] * 26
        for c in s:
            idx = ord(c) - ord("a")
            hist[idx] += 1
        return hist
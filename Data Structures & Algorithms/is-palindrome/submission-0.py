class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        for c in s:
            if not c.isalnum():
                s = s.replace(c, "")
    
        bs = ""
        for c in reversed(s):
            if c.isalnum():
                bs += c 
        return s == bs
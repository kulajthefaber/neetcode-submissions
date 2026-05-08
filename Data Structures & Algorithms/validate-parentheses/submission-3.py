class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # It's a closing bracket: peek at the stack
                top_element = stack.pop() if stack else '#'
                
                # Check if the opener matches
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket: push it
                stack.append(char)

        # If stack is empty, all brackets were matched correctly
        return not stack




    # def isPair(self, s1:str, s2:str) -> bool:
    #     if s1 == "[" and s2 == "]":
    #         return True
    #     if s1 == "(" and s2 == ")":
    #         return True
    #     if s1 == "{" and s2 == "}":
    #         return True
    #     return False

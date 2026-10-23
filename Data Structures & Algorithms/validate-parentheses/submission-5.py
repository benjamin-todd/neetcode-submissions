class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                char = stack.pop()
                if char == "(" and i != ")":
                    return False
                elif char == "[" and i != "]":
                    return False
                elif char == "{" and i != "}":
                    return False
        
        if len(stack) != 0:
            return False
        return True
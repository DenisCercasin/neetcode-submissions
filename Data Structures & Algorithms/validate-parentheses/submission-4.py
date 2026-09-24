class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        answer = False
        for char in s:
            if char in {"{","(","["}:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char==")":
                    if stack[-1]!="(":
                        return False
                elif char=="]":
                    if stack[-1]!="[":
                        return False
                elif char=="}":
                    if stack[-1]!="{":
                        return False
                stack.pop()
        return True if not stack else False
class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            "}":"{",")":"(","]":"["
        }
        stack = []
        for character in s :
            if character in mapping:
                if stack:
                    if stack.pop() != mapping[character]:
                        return False
                else:
                    return False
            else:
                stack.append(character)
        if stack:
            return False
        return True


class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for character in s:
            if character in ["(",'{','[']:
                ans.append(character)
            else:
                if ans:
                    if character == "]":
                        if ans[-1] != '[':
                            return False
                        
                    elif character == "}":
                        if ans[-1] != '{':
                            return False
                    else:
                        if ans[-1] != '(':
                            return False
                    ans.pop(-1)
                else:
                    return False
        if ans:
            return False 
        return True

        
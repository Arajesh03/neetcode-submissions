class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stk.append(c)
            else:
                if not stk or stk.pop() != pairs[c]:
                    return False
        
        return not stk
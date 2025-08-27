def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  # closing -> opening map
    
    for char in s:
        if char in mapping:  # closing bracket
            top = stack.pop() if stack else '#'  # stack empty case
            if mapping[char] != top:
                return False
        else:  # opening bracket
            stack.append(char)
    
    return not stack  # stack should be empty if valid


# ---------- testing ----------
print(isValid("[{()}]"))   # True
print(isValid("()[]{}"))   # True
print(isValid("(]"))       # False
print(isValid("([)]"))     # False
print(isValid("{[]}"))     # True

Output

True
True
False
False
True

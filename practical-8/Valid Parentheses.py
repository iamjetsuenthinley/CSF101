def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map:  
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else: 
            stack.append(char)
    
    return len(stack) == 0


example1 = "()[]{}"
example2 = "(]"
example3 = "([{}])"

print(example1, "=>", isValid(example1))
print(example2, "=>", isValid(example2))
print(example3, "=>", isValid(example3))

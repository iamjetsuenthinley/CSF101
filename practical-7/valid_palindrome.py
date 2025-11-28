def ispalindrome(s):
    left, right = 0, len(s)-1

    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right+=1
        left=+1
        right=-1
        
        if s[left].lower()!=s[right].lower():
            return False
    
    return True

text=input("Write something: ")
print(f"Is Palindrome: {ispalindrome(text)}")
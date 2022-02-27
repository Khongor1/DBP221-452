def isPalindrome(value):
    rev = ''.join(reversed(value))
    if (value==rev):
        return True
    else:
        return False
value= "molom"
ans=isPalindrome(value)
if (ans):
    print("This is absolutely a palindrome")
else:
    print("No, man!")


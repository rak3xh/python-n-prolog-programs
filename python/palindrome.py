def is_palindrome(s):
    return s == s[::-1]


s = input("Enter the S\string to be checked:")
if is_palindrome(s):
    print("The string is Palindrome!!")

else:
    print("The string is not palindrome!!")

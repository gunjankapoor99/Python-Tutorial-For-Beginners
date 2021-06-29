def palindrome(str1):
    rev = str1[::-1]
    if (rev==str1):
        print("true")
    else:
        print("false")

str1 = input("Enter a string: ")
palindrome(str1)

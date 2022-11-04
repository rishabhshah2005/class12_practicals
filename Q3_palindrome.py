#Q3.Create function to check whether string is Palindrome or not.

inp = input("Enter string: ")

if inp == inp[::-1]:
    print("The sring is palindrome!!")

else:
    print("The string is not palindrome")
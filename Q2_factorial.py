#Q2. Create a function to find the factorial of a number.

num = int(input("Find factorial of: "))

ans = 1
if num==0:
    print(1)

else:
    for i in range(1, num+1):
        ans *= i
    print(ans)
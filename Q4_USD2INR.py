# Q4.Create function to convert INR to USD or USD to INR.

print("1. USD TO INR")
print("2. INR TO USD")

index = input("Enter index: ")

if index == '1':
    num = int(input("Enter number: "))
    ans = num*80
    print("$", num, " is ", ans, " rupees")

else:
    num = int(input("Enter number: "))
    ans = num/80
    print(num, "rupees is $", ans)

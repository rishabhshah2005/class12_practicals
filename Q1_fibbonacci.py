# Q1. Create a function to display fibonacci series.

def fibonacci(lim):
    print(0)
    print(1)
    last = 1
    seclast = 0
    for i in range(0, lim-1):
        sum = last+seclast
        print(sum)
        seclast = last
        last = sum

num = int(input("Show first?...: "))
fibonacci(num)
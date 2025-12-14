def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial (x - 1)

# Taking input from user at runtime
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("The factorial of", num, "is", factorial(num))

<<<<<<< Updated upstream
def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def repeat():
    a=input("\nDo you want to continue (Y/N): ")
    if a == 'Y' or a=='y':
        n = int(input("Enter the number : "))
        print(f"The Fibonacci number of {n} is : ",fibo(n))
        repeat()
    else:
        print("Program Stopped")

n = int(input("Enter the number : "))
print(f"The Fibonacci number of {n} is : ",fibo(n))
=======
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def repeat():
    a = input("\nDo you want to continue yes or no : ")
    if a == "yes":
        n = int(input("Enter a number: "))
        result = fibonacci(n)
        print("Fibonacci of", n, "is", result)
        repeat()
    else:
        print("Program Stopped")
    
    
n = int(input("Enter a number: "))
result = fibonacci(n)
print("Fibonacci of", n, "is", result)
>>>>>>> Stashed changes
repeat()

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

def repeat():
    a=input("\nDo you want to continue (Y/N): ")
    if a == 'Y' or a=='y':
        n = int(input("Enter the number : "))
        print(f"The Factorial of {n} is : ",fact(n))
        repeat()
    else:
        print("Program Stopped")

n = int(input("Enter the number : "))
print(f"The Factorial of {n} is : ",fact(n))
repeat()

class Stack_Adt:
    def __init__(self):
        self.stack=[]
        self.size=int(input("Enter the limit:"))
    def Push(self):
        
        if len(self.stack)>=self.size:
            print("The Stack is Overflow:")
        else:
            for i in range(0,self.size):
                item=input("Enter the item:")
                self.stack.append(item)
                print(f"Given item is Pushed:=>{item}")
        print(self.stack)
    def Pop(self):
        if len(self.stack)==0:
            print("Stack is Underflow:")
        else:
            g=self.stack.pop()
            print(f"Given item is Popped:=>{g}:")
        print(self.stack)
    def disp(self):
        if len(self.stack)==0:
            print("Stack is Underflow")
        else:
            print(f"The current Stack:{self.stack}")
  
s=Stack_Adt()

def rep():   
    while True:
        print("Given Choices are available\n1 is Push Function\n2 is Pop Function\n3 is Display Function\n4 is Exit the process")
        f=int(input("Enter the Choice:"))
        if f==1:
            s.Push()
        elif f==2:
            s.Pop()
        elif f==3:
            s.disp()
        elif f==4:
            print("Exit the Process:")
            break
rep()
while True:
    
    d=input("Do you want to continue?:/nType yes or no:")
    if d=="yes":
        rep()
    elif d=="no":
        print("The Stack Process was Stopped!")
        break
    else:
        print("Invalid Typing")


    



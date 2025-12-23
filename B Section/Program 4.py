class Queue_Adt:
    def __init__(self):
        self.queue=[]
        self.size=int(input("Enter the limit:"))
        
    def Enqueue(self):
        if len(self.queue)>=self.size:
            print("The Queue is Full:")
        else:
            for i in range(0,self.size):
                item=input("Enter the item:")
                self.queue.append(item)
                print(f"Given item is Added the Queue:=>{item}")

    def Dequeue(self):
        if len(self.queue)==0:
            print("Queue is Empty:")
        else:
            g=self.queue.pop(0)
            print(f"Given item is Removed the Queue:=>{g}:")

    def disp(self):
        if len(self.queue)==0:
            print("Queue is Empty")
        else:
            print(f"The current Queue:{self.queue}")
  
s=Queue_Adt()

def rep():   
    while True:
        print("Given Choices are available\n1 is Adding the Element in Queue \n2 is Removing Element in Queue\n3 is Display the Queue\n4 is Exit the process")
        f=int(input("Enter the Choice:"))
        if f==1:
            s.Enqueue()
        elif f==2:
            s.Dequeue()
        elif f==3:
            s.disp()
        elif f==4:
            print("Exit the Process:")
            break
rep()
while True:
    
    d=input("Do you want to continue?:\nType yes or no:")
    if d=="yes":
        rep()
    elif d=="no":
        print("The Queue Process was Stopped!")
        break
    else:
        print("Invalid Typing")


    



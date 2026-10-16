class node:
    def __init__ (self,data,next=None):
        self.data=data
        self.next=None

head=node(10)
second=node(15)
third=node(20)
fourth=node(30)

head.next=second
second.next=third
third.next=fourth

def  show(head):
    temp=head
    while temp !=None:
        print(temp.data,end=" ")
        temp=temp.next
    print(None)

print("original list") 
print(head.next.next)   
target=30
new=node(25)
temp=head
while temp.next.data !=target:
    temp=temp.next
new.next=temp.next
temp.next=new
print("\nAfter inserting 25 at position 3")
show(head)

 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)

head.next=second; second.prev=head
second.next=third; third.prev=second
third.next=fourth; fourth.prev=third

def show(head):
    temp=head
    print("forward:",end=" ")
    print("None",end="<->")
    while temp !=None:
        print(temp.data,end="<->")
        last=temp
        temp=temp.next

    print("None")
    print("backward:",end=" ")
    print("None",end="<->")

    temp=last
    while temp !=None:
        print(temp.data,end="<->")
        temp=temp.prev
    print("None")
print("original list")
show(head)

new=Node(5)
new.next=head
head.prev=new
head=new
print("\nAfter inserting 5 at start:")
show(head) 
last=Node(50)
temp=head
while temp.next !=None:
    temp=temp.next
temp.next=last
last.prev=temp
print("\nAfter insertin 50 at end")
show(head) 

target=30
new=Node(25)
temp=head
while temp.next.data!=target:
    print(temp.data)
    temp=temp.next
    
temp.next.prev=new
new.next=temp.next
temp.next=new
new.prev=temp    
print("\nAfter inserting 25 at position 3")
show(head)
    




        

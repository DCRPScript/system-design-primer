'''class node:
    def __init__ (self,data,next=None):
        self.data=data
        self.next=None

head=node(10)
second=(15)
third=(20)
fourth=(30)

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
print(temp.next.next)  '''  


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
    while temp !=None:
        print(temp.data,end="<->")
        temp=temp.next

    print("None")
    print("backward:",end=" ")
    temp=last
    while temp !=None:
        print(temp.data,end="<->")
        temp=temp.prev
    print("None")
    print("original list")
    show(head)         



        

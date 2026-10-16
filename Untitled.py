class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def show(head):
    temp = head

    while temp is not None:
        print(temp.data,end=" => ")
        temp = temp.next

        if temp == head:
            break

head = Node(10)
sec = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

head.next = sec
sec.next = third
third.next = fourth
fourth.next = fifth
fifth.next = head

new = Node(00)
new.next = head


show(head)
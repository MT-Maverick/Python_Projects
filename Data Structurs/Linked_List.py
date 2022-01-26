#The Node template:
class Node:
    def __init__(self,data=None):
        self.data=data
        self.link=None

#The linked-lists template:
class List:
    def __init__(self):
        self.head=None
    # Method to displayes every element in the linked list:
    def printer(self):
        printer=self.head
        while self.head !=None:
            print(printer.data)
            printer=printer.link

    # Method to insert at the begining of the linked list:
    def AtBegining(self,NewData):
        Nnode= Node(NewData)
        Nnode.link = self.head
        self.head =Nnode
    
    # Method used to insert a node at the end of the list:
    def AtEnd(self,NewData):
        Nnode=Node(NewData)
        if self.head ==None:
            self.head=Nnode
            return
        last =self.head
        while(last.link):
            last =last.link
        last.link=Nnode

    # Method used to insert a node between specified location within the list:
    def InBetween(self,Position,NewData):
        if Position == None:
            print("NODE NOT FOUND")
            return
        Nnode =Node(NewData)
        Nnode.link = Position.link
        Position.link = Nnode
    
    # Method used to remove a node within the list:
    def Remove(self,key_value):
        head = self.head
        if(head!=None):
            if(head.data==key_value):
                self.head = head.link
                head=None
                return
            while(head!=None):
                if(head.data==key_value):
                    break
                before =head
                head =head.link
            if(head==None):
                return
            before.link =head.link
            head=None


#The instanciation the list:
list_item = List()

list_item.head =Node("Hello") 

list_item.AtBegining("Created By Mfundo Sindane:")

list_item.AtEnd("Let's Breakdown my name:")
list_item.AtEnd("M-Motivated")
list_item.AtEnd("F-Focused")
list_item.AtEnd("U-Unique")
list_item.AtEnd("N-Negative") # Removed Word
list_item.AtEnd("N-New")
list_item.AtEnd("D-Driven")
list_item.AtEnd("O-Original")

list_item.Remove("N-Negative") 
list_item.InBetween(list_item.head.link.link,"----------------------------------")

list_item.printer()

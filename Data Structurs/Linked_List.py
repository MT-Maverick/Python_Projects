#The Node used as a template for every node in the list:
class Node:
    def __init__(self,data=None):
        self.data=data
        self.link=None

#The Blueprint for linked-lists capabilities:
class List:
    def __init__(self):
        self.head=None
    #The print function used to displayes every element in the linked list:
    def printer(self):
        printer=self.head
        while self.head !=None:
            print(printer.data)
            printer=printer.link
    #The function used to insert a variable at the begining of the linked list:
    def AtBegining(self,NewData):
        Nnode= Node(NewData)
        Nnode.link = self.head
        self.head =Nnode
    #The function used to set a node at the end of the list:
    def AtEnd(self,NewData):
        Nnode=Node(NewData)
        if self.head ==None:
            self.head=Nnode
            return
        last =self.head
        while(last.link):
            last =last.link
        last.link=Nnode
    
    def InBetween(self,Position,NewData):
        if Position == None:
            print("NODE NOT FOUND")
            return
        Nnode =Node(NewData)
        Nnode.link = Position.link
        Position.link = Nnode



#The instanciation of every node in the list:
list_item = List()
list_item.head =Node("Hello")
list_item0 =Node("I made this")

#The linkage of every node to its respective link:
list_item.head.link =list_item0

#Method to inserted node AtBegining: 
list_item.AtBegining("Created By Mfundo Sindane:")

#Method to inserted node AtEnd: 
list_item.AtEnd("You can too")

#If the node is inserted inbetween: 
list_item.InBetween(list_item.head,"----------------------------------")

#the iteration of every node:
list_item.printer()

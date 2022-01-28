#Creating a stack using a list:
stack=[]
stack.append("Mfundo")
stack.append("IS")
stack.append("A")
stack.append("Really")
stack.append("Good")
stack.append("Programmer")
"""
print("initial stack elements:")
print(stack,"\n")

for i in stack:
    print(i)

stack.clear()

print("\nstack elements after:")
print(stack)

"""
#Stack implemented using deque:
from collections import deque

stack =deque()

stack.append("Mfundo")
stack.append("Is")
stack.append("A")
stack.append("Really")
stack.append("Good")
stack.append("Programmer")

for stack in stack:
    print(stack.pop())

print(stack)

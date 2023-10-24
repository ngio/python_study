# Python program to
# demonstrate stack implementation
# using list
 
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty


"""
    A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.
    
    The functions associated with stack are:
    
    empty() – Returns whether the stack is empty – Time Complexity: O(1)
    size() – Returns the size of the stack – Time Complexity: O(1)
    top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
    push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
    pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
    Implementation:
    There are various ways from which a stack can be implemented in Python. This article covers the implementation of a stack using data structures and modules from the Python library. 
    Stack in Python can be implemented using the following ways: 
    
    list
    Collections.deque
    queue.LifoQueue
"""




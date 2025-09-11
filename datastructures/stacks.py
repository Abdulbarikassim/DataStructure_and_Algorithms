"""
Stack - This is a data structure that stores ordered data and  that uses LIFO(last In First Out).
Its like a list but this allows data to be added or removed from top of the stack.
OOP - we use object-oriented programming to achieve.

** Operations of a stack.
- Pushing and popping items: order of one time complexity meaning constant time O(1).

Question is why choose a stack instead of a list:
- A stack is a list with fewer restrictions but by  restricting this data type like this makes it very fast.
Below is the operation and there time complexity:
- push: O(1).
- pop:O(1).
- peek: O(1).
- size: O(1).

** Stack review:
- stack operations are limited: no searching, no sorting, no random access.
- stack like any data type can store any type of data, what makes it a stack is the operation but not the
    the type of data it stores.
- All supported operations are O(1).

Stacks can be used in real world:
- to manage function calls.
- undo/redo funcitonality.
- Expression evalution.
- browser history.
"""


# implementation.

class Stack():
    # initialize the stack
    def __init__(self ):
        self.items = []

    def push(self, item):
        self.items.append(item)
    # return the size of the stack
    def size(self):
        if len(self.items) == 0:
            return None
        return len(self.items)
    # get the last item and don't modify the stack
    def peek(self):
        if len(self.items) == 0:
            return None

        return self.items[-1]
    # return the last items and remove from the list.
    def pop(self):
        if len(self.items) == 0:
            return None


        return self.items.pop()

    def print_stack(self):
        if len(self.items) == 0:
            print("-empty")
            return
        for items in reversed(self.items):
            print(items)


stack = Stack()
print(stack.peek())

stack.push("Abdulbari")
stack.push("maimuna")
stack.push("mohamed")
stack.print_stack()

print(stack.size())

print(stack.peek())
print(stack.pop())
stack.print_stack()






























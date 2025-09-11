"""
# Queue
- is a fundamental data structure in computer science that is used for storing and managing data.
- They follow the format first in first out.
- Operation are very fast all O(1):
    - Enqueue: adding items at end.
    - Dequeue: removing item at front.
    - peek.
    - getFront: get the item at the front without deleting it.
    - getRear: get the item at the end without deleting.
    - size: get the size of the queue.
    - isEmpty: return true or false based on if there is something in the queue.
# Usage:
- used in operating systems: CPU scheduling and memory management.
- in algorithms like bfs of graph and level order traversal of a tree.
"""



class Queue:
    def __init__(self):
        self.items = []

    # get the size of queue.
    def size(self):
        return len(self.items)

    # add items at end also enqueue.
    def push(self, item):
        return self.items.append(item)

    # get the item at the front.

    def get_front(self):
        if self.size() == 0 :
            return None

        return self.items[0]


    # get and remove the item at front also known as dequeue.

    def dequeue(self):
        if self.size() == 0:
            return None

        return self.items.pop(-1)



    def display(self):
        print(','.join(map(str, self.items)))




queue = Queue()
queue.push(10)
queue.push(20)
queue.push(40)
queue.push(50)
queue.display()

print("front number: ", queue.get_front())
print("Rear number: ", queue.dequeue())

queue.display()





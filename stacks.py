# Stack - This is a data structure that uses LIFO(last In First Out).
# OOP - we use object-oriented programming to achieve.

class Stack:
    def __init__(self):
        self.items = []

    # Method to check if its empty.

    def is_empty(self):
        return not self.items

    #     add an items.

    def add_item(self, item):
        self.items.append(item)




    def remove(self):
        if self.is_empty():
            raise ValueError("List is empty")
        else:
            return self.items.pop()

    # check the last items in the list.

    def peek(self):
        return self.items[-1]

    #     size of the list

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()


    s.add_item(3,2,2,2)
    print(s)



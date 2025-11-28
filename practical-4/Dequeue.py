from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def insert_front(self, item):
        self.items.appendleft(item)

    def insert_rear(self, item):
        self.items.append(item)

    def delete_front(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Deque is empty")

    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Deque is empty")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is empty")

    def size(self):
        return len(self.items)


deque = Deque()
deque.insert_front("A")
deque.insert_rear("B")
deque.insert_front("C")

print(deque.delete_front())  
print(deque.delete_rear())   
print(deque.get_front())    
print(deque.size())         

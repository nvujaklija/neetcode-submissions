class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        self.min = None
class MinStack:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, value: int) -> None:
        new = Node(value)
        
            
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        
        new.min = new
        if self.head.next.min:
            current_min = self.head.next.min
            if value>current_min.value:
                new.min = current_min
        self.head.next = new
        



    def pop(self) -> None:
        top = self.head.next
        self.head.next = top.next
        top.next.prev = self.head

    def top(self) -> int:
        return self.head.next.value

    def getMin(self) -> int:
        return self.head.next.min.value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
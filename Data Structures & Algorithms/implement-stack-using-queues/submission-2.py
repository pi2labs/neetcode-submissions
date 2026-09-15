class MyStack:
    from collections import deque
    def __init__(self):
        self.stack = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        while self.stack:
            self.temp.append(self.stack.popleft())

        self.stack.append(x)

        while self.temp:
            self.stack.append(self.temp.popleft())
        
    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:  
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
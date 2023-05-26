from copy import copy


class Stack:
    
    def __init__(self, *args) -> None:
        """
        Stack()             == _stack[]
        Stack(x)            == _stack[x]
        Stack(xs)           == _stack[x, xs]
        Stack(bad, values)  == ValueError
        """
        self._stack = []
            
        if len(args) == 1 and isinstance(args[0], list):
            self._stack = args[0]
        elif len(args) == 1:
            self._stack.append(args[0])
        elif len(args) >= 1:
            raise ValueError("Invalid arguments")

    def clone(self):
        new_stack = Stack()
        new_stack._stack = copy(self._stack)
        return new_stack
    
    def duplicate(self) -> None:
        top_value = self.pop()
        self.push(top_value)
        self.push(top_value)
        
    def is_empty(self) -> bool:
        if len(self._stack) == 0:
            return True
        else:
            return False

    def peek(self) -> any:
        return self._stack[-1]
    
    def pop(self) -> any:
        return self._stack.pop(-1)

    def push(self, value) -> None:
        self._stack.append(value)
    
    def safe_pop(self) -> any:
        if self.is_empty():
            return None
        else:
            self.pop()

    def swap(self) -> None:
        first = self.pop()
        second = self.pop()
        
        self.push(first)
        self.push(second)

    def __len__(self):
        return len(self._stack)

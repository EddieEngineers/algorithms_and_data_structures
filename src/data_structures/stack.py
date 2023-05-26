from copy import copy


class Stack:
    
    _stack = []
    
    def __init__(self) -> None:
        pass
    
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

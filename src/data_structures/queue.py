class Queue:
    _queue = []

    def dequeue(self) -> any:
        return self._queue.pop(0)

    def enqueue(self, value) -> None:
        self._queue.append(value)
        
    def first(self) -> any:
        return self._queue[0]
    
    def last(self) -> any:
        return self._queue[-1]

    def __len__(self):
        return len(self._queue)

class Deque:
    _queue = []
    
    def __len__(self) -> int:
        return len(self._queue)
    
    def push_front(self, value) -> None:
        self._queue.insert(0, value)
    
    def push_back(self, value) -> None:
        self._queue.append(value)
        
    def pop_front(self) -> any:
        return self._queue.pop(0)
    
    def pop_back(self) -> any:
        return self._queue.pop(-1)
    
    def peek_front(self) -> any:
        return self._queue[0]

    def peek_back(self) -> any:
        return self._queue[-1]

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

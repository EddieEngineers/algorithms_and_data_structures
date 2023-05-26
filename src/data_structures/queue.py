class Queue:
    _queue = []

    def enqueue(self, value) -> None:
        self._queue.append(value)
    
    def dequeue(self) -> any:
        return self._queue.pop(0)

    def __len__(self):
        return len(self._queue)

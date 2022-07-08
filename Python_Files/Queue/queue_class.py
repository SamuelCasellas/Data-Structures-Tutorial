class Queue:
    def __init__(self) -> None:
        """Create an empty queue.
        """
        self._queue = list()
    
    def enqueue(self, item) -> None:
        self._queue.append(item)

    def deque(self):
        try: return self._queue.pop(0)
        except IndexError: return "Nothing in the queue"
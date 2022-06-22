class Queue:
    def __init__(self, limit=None, shift_when_full=False):
        """Create a queue where a limit for the number of items can be set 
        that when reached will either the first item will automatically be popped 
        as the new item is appended or the item cannot be appended at all based on
        the boolean value for shift_when_full.
        """
        self._queue = list()
        self._limit = limit
        self._shift_when_full = shift_when_full
    

    def queue(self, item):
        if self._limit is None or self._limit > len(self):
            self._queue.append(item)
        # Full capacity has been reached
        elif self._shift_when_full:
            self._queue.append(item)
            self.deque()
        # If the queue is full and shift option is off, do nothing.

    def deque(self):
        try: return self._queue.pop(0)
        except IndexError: return "Nothing in the queue"

    def __len__(self):
        return len(self._queue)

    def __iter__(self):
        for item in self._queue:
            yield item
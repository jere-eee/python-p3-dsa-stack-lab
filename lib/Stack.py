class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            return len(self.items) - 1 - self.items.index(target)
        except ValueError:
            return -1

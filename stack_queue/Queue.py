from list import List


class Queue(List):
    def push(self, value):
        return super(Queue, self).push(value)

    def pop(self, pos=None):
        return super(Queue, self).pop(pos)

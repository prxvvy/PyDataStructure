from list import List


class Stack(List):
    def push(self, value):
        return super(Stack, self).push(value)

    def pop(self, pos=None):
        return super(Stack, self).pop(pos)

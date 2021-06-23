class Stack(object):
    """Stack Project With Python"""
    def __init__(self, size):
        self._stack = []
        self.size = size

    def push(self, item):
        if len(self._stack) < self.size:
            self._stack.append(item)
        else:
            raise Exception ('Stack is full')
    
    def pop(self):
        try:
            return self._stack.pop()
        except:
            raise Exception('Stack was empty')

if __name__ == '__main__':
    a = Stack(4)
    a.push(1)
    a.push(4)
    print(a.pop())




class Queue(object):
    """Queue Project With Python"""
    def __init__(self, size):
        self._queue = []
        self.size = size

    def push(self, item):
        if len(self._queue) < self.size:
            self._queue.append(item)
        else:
            raise Exception ('Queue is full')
    
    def pop(self):
        try:
            return self._queue.pop(0)
        except:
            raise Exception('Queue was empty')

if __name__ == '__main__':
    a = Queue(4)
    a.push(1)
    a.push(4)
    print(a.pop())


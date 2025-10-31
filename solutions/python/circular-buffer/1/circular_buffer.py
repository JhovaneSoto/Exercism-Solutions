class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message=message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message=message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity=capacity
        self.buffer=[None]*capacity
        self.ultimo=0
        self.siguiente=0
        self.tam=0

    def read(self):
        if self.tam==0:
            raise BufferEmptyException("Circular buffer is empty")
            
        out = self.buffer[self.ultimo]
        self.ultimo=(self.ultimo+1)%self.capacity
        self.tam-=1
        return out
        
    def write(self, data):
        if self.tam==self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.siguiente]=data
        self.siguiente=(self.siguiente+1)%self.capacity
        self.tam+=1

    def overwrite(self, data):
        if self.tam==self.capacity:
            self.buffer[self.siguiente]=data
            self.siguiente=(self.siguiente+1)%self.capacity
            self.ultimo=(self.ultimo+1)%self.capacity
        else:
            self.write(data)

    def clear(self):
        self.buffer=[None]*self.capacity
        self.ultimo=0
        self.siguiente=0
        self.tam=0

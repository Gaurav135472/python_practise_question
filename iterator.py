class Fibonaki_Iterator:
    
    def __init__(self,limit):
        
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result 
            self.n += 1
            return result
        else:
            raise StopIteration
        
fib_iter = iter(Fibonaki_Iterator(8))

while True:
    try:
        print(next(fib_iter))
    except:
        break
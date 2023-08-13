#Aim : Implementing Iterable
"""Class to implement an iterator of powers of two"""

class PowTwo:
    def __init__(self, max = 0):    #constructor
        self.max = max

    def __iter__(self):
        self.n = 1 
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
            

#program
print("Power of 2's are:")
x=PowTwo(10)
for i in x:
    print(i, end=' ')
print()

y=PowTwo(2)#max=1
y_iter=iter(y)
print(next(y_iter))     #2^1 
print(next(y_iter))     #2^2















#Aim : Implementing Iterators and its tools with sequences

colors=['red','green','blue','black','orange','pink',\
        'maroon','gray','navy']
print('\nUsing iter() and next()')
colors_iter=iter(colors)
val=1
while val==1:
    print(next(colors_iter))
    val=int(input("Enter 1 for next element or 0 for exit:"))
    
#cycle
from itertools import cycle
print('\nUsing cycle() and next()')
colors_cycle=cycle(colors)
val=1
while val==1:
    print(next(colors_cycle))
    val=int(input("Enter 1 for next element or 0 for exit:"))

    
#islice: finite sequences from infinite sequences
from itertools import islice
print('\nUsing islice() making finite set')
colors_cycle=cycle(colors)            # infinite
limited = islice(colors_cycle, 0, 14) # finite
#print(list(limited))
for x in limited:                     # so safe to use for-loop on
    print(x)


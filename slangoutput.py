import math

def iseven(x):
    return x / 2 == round(x / 2)


if iseven(10) == True:
    print('10 is even')
else:
    print('How did u make 10 not even')
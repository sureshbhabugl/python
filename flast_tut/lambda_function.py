# Lambda functions are functions that does not have a name but return values.
from typing import Sequence


def add(x, y):
    return x+y


print(add(5, 7))

print((lambda x, y: x+y)(5, 7))  # this is the lambda of add


# Map function

def double(x):
    return x * 2


sequence = [1, 2, 3, 4, 5, 6]
doubled = [double(x) for x in sequence]
print(doubled)
# Using maps
doubled = list(map(double, sequence))
print(doubled)
# Using lambda
doubled = list(map(lambda x: x*2, sequence))

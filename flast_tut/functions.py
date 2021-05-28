def add(x, y):
    print(x+y)


add(3, 5)

"""Keyword/Named arguement"""


def say_hello(surname="Bob", name="Smith"):
    pass


"""Default Parameters:"""


def add(x, y=8):  # Here y has an optional parameter.
    print(x+y)


add(5)

# add(y=5) This is an error as the positional parameter is not passed.

"""
Example of NONE
NONE is the default returned value if a function does not have a return value.
In the above example, add() prints a value but does not returns any. When you try to print add inside a print, you'll see None.
"""
print(add(1, 2))

# docstrings explain what a function does in popup menu

def example_docstring():
    """This function does absolutely nothing at all."""
    print("Absolutely nothing")
    return False


# hover mouse over it
example_docstring()


# important!!
# you can use a DICTIONARY to mimic function pointers in c
# example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {  # assume the values are valid function names
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

function = operations["*"]
function(2, 3)  # <--- this will call multiply function with parameters 2, 3

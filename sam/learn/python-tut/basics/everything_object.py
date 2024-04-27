# Everything is an object 
# Define a custom function
def greet(name):
    """This function greets the user."""
    return "Hello, " + name + "!"

# Define a custom class
class MyClass:
    """This is a custom class."""
    def __init__(self, x):
        self.x = x
    
    def display(self):
        """This method displays the value of x."""
        print("Value of x:", self.x)

# Define some variables
i = 10
f = 3.14
s = "Hello"
b = True
lst = [1, 2, 3]
tup = (4, 5, 6)
dct = {'a': 1, 'b': 2}
obj = MyClass(7)

# Define a list of various objects
objects = [i, f, s, b, lst, tup, dct, obj, greet]

# Iterate through each object and explore its attributes
for obj in objects:
    print("\nObject:", obj)
    print("Type:", type(obj))
    print("Attributes:")
    print(dir(obj))
    print("Documentation:")
    print(obj.__doc__)

"""
This is a simple Python script that defines a function to greet a user and another function to add two numbers. 
It then calls these functions and prints the results.
"""

def greet(name):
    print(f"Hello, {name}!")

greet("World")

a = 2
b = 3
def add(a, b):
    return(a+b)

result = add(a, b)
print(result)
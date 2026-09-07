"""
This is a simple Python script that defines a function to greet a user and another function to add two numbers. 
It then calls these functions and prints the results.
"""

def greet(name):
    print(f"Hello, {name}!")

greet("World")

a = 8
b = 3
def add(a, b):
    return(a+b)
def subtract(a, b):
    return a - b

addResult = add(a, b)
subtractResult = subtract(a, b)
print(addResult)
print(subtractResult)


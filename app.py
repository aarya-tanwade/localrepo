print("Hello, World!")

def greet(name):
    return f"Hello, {name}!"

name = "Aarya"
greeting = greet(name)
print(greeting)

def add(a, b):
    return a + b

result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}") 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
number = 5
fact_result = factorial(number)
print(f"The factorial of {number} is: {fact_result}")

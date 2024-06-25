# Programming Challenge: Factorial
# Create a function which takes one positive integer as its input and returns its factorial.
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is returned by those calls. 
# For those inputs, you should get 6, 24, and 120, respectively.

def factorial_counter(number):
    factorial = 1
    for num in range(number, 1, -1):
        factorial *= num
    return factorial

print(factorial_counter(3))
print(factorial_counter(4))
print(factorial_counter(5))
# Strings Exercises
# Do all of this in a .py file in Pycharm
# 1. Create a variable and assign it the string "Just do it!"
#       012345678910
moto = "Just do it!"

# 2. Access the "!" from the variable by index and print() it
print(moto[10])

# 3. Print the slice "do" from the variable
print(moto[5:7])

# 4. Get and print the slice "it!" from the variable
print(moto[8:])

# 5. Print the slice "Just" from the variable
print(moto[:4])

# 6. Get the string slice "do it!" from the variable and concatenate it with the string "Don't ". 
#    Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
edited = "Don't " + moto[5:]
print(edited)


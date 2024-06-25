# del and list methods exercises
# Do all of this in a .py file in Pycharm.
# 1. Create a variable called arctic_animals and assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
acrtic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

# 2. Use del to remove "tiger" from the list assigned to arctic_animals.
del acrtic_animals[4]

# 3. Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.
acrtic_animals.remove("elephant")

# 4. Use the .append() method to add the string "arctic fox" to the list arctic_animals.
acrtic_animals.append("arctic fox")

# 5. Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.
acrtic_animals.insert(3, "snowy owl")

# 6. Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.
acrtic_animals.sort()

# 7. Use print() to display the list assigned to arctic_animals
print(acrtic_animals)

# 8. Use .index() to get the index number of "reindeer" from arctic_animals then print it.
print(acrtic_animals.index("reindeer"))

# 9. Use .pop() to get the last item from the list arctic_animals then print it.
print(acrtic_animals.pop())
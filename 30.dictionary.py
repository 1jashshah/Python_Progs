# introduction to dictionaries exercises
# Do all of this in a .py file in Pycharm.

# 1. create a variable and assign it a dictionary that has 5 key value pairs
star_wars = {
    "Luke" : "Skywalker",
    "Obi-Wan" : "Kenobi",
    "Haan" : "Solo",
    "Darth" : "Maul",
    "Mon" : "Mothma"
}

# 2. print and access the value held at the third key in the dictionary
print(star_wars["Haan"])

# 3. use the in keyword to check if a key appears in the dictionary and print the result
print("Darth" in star_wars)

# 4. use not in to check if a key does not appear in the dictionary and print the result
print("Rey" not in star_wars)
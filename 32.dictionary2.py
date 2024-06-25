# dictionary methods 2 exercises
# Do all of this in a .py file in Pycharm.

# 1. use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and the string "consonant" as the value for each of those keys.  
# Only use lower case letters for the consonants.  "y" counts as a consonant for this exercise.  Use a for loop and the .items() method to print each of those key: value pairs on a different line.  
# For example, the first 3 lines in the output should be the following:
#   b consonant
#   c consonant
#   d consonant
consonants_dict = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
for letter, key in consonants_dict.items():
    print(letter, key)

# 2. paste this dictionary into your .py file then pop and print "Big Mac" from it
#    fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))

# 3. use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items then print new fast_food_items dictionary.
fast_food_items.popitem()
print(fast_food_items)
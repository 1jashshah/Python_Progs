# indexes and list slicing exercises
# Do all of this in a .py file in Pycharm.

# 1. Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
var_list = [[0, 2], [4, 6], [8, 10], [12, 14]]

# 2. Access the first list from the list of lists in step 1 by index then print it.
print(var_list[0])

# 3. Access the 14 from the list in step 1 then print it.
print(var_list[3][1])

# 4. Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
var_items = ["chair", "table", "desk", "lamp", "bed"]

# 5. Use a negative integer to access "chair" from the variable in step 4 by index then print it.
print(var_items[-5])

# 6. Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.
print("Most people own at least " + str(var_list[0][1]) + " " + var_items[0] + "s.")

# 7. Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
var_float = [0.98, 8.76, 6.54, 4.32]

# 8. Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
print(var_float[1:])

# 9. Print the slice [8.76, 6.54] from the variable you created in step 7.
print(var_float[1:3])

# 10. Print the slice [0.98, 8.76] from the variable you created in step 7.
print(var_float[:2])

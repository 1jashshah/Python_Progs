# Get user input for length, width, and height
length = int(input("Enter an integer that represents length in feet: "))
width = int(input("Enter an integer that represents width in feet: "))
height = int(input("Enter an integer that represents height in feet: "))

# Define the function to calculate the volume
def prism_vol(l, w, h):
    return l * w * h

# Calculate the volume and print the result
print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")

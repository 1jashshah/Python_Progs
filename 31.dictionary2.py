# dictionary methods 1 exercises
# Do all of this in a .py file in Pycharm.

# 1. create a variable and assign it the following dictionary:
#    {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# 2. make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

music = {"Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"
         }

# 3. print the length of the dictionary.
print(len(music))

# 4. use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for singer in music.keys():
    print(singer)

# 5. print all of the values from the dictionary using the .values() method.
for song in music.values():
    print(song)

# 6. use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for singer, song in music.items():
    print(singer, song)

# 7. use the .get() method to check the dictionary for the key
#    "Promise of the Real"
#    and create a message that will print if the key is not found in the dictionary.
print(music.get("Promise of the Real", "Promise of the Real is not in the given dictionary"))
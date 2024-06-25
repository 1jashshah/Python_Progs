message = "Harsh"
print(message + " -> upper() -> "+ message.upper())
print(message + " -> lower() -> "+ message.lower())
print(message + " -> isupper() -> " + str(message.isupper()))
print(message.upper() + " -> isupper() -> " + str(message.upper().isupper()))
print(message + " -> islower() -> " + str(message.islower()))
print(message.lower() + " -> islower() -> " + str(message.lower().islower()))

message = "Harsh"
print(message + " -> isalpha() -> "+ str(message.isalpha()))

message = "H2r4h"
print(message + " -> isalnum() -> "+ str(message.isalnum()))

message = "12345"
print(message + " -> isdecimal() -> "+ str(message.isdecimal()))

message = "     "
print(message + " -> isspace() -> "+ str(message.isspace()))

message = "Harsh"
print(message + " -> istitle() -> "+ str(message.istitle()))

message = "Harsh Patil"
print(message + " -> .startswith(\"Ha\") -> "+ str(message.startswith("Ha")))

message = "Harsh Patil"
print(message + " -> .endswith(\"il\") -> "+ str(message.endswith("il")))

print(" ".join(["Harsh", "Ashok", "Patil"]))
print("".join(["Harsh", "war", "dhan"]))

print("Reverse-Flash, Zoom, Savitar".split(", "))
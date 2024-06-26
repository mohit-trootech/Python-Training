"""
format: function is used to format the string with corresponding variables
"""
# Unformatted String
name_str = "Hello {name}!, Age: {age}"
num_str = "Hello {0}!, Age: {1}"
empty_str = "Hello {}!, Age: {}"

print(name_str.format(name="Mohit", age=23))  #Named Indices
print(num_str.format("Mohit", 23))  #Number Indices
print(num_str.format("Mohit", 23))  #Empty Indices

# Formatting Types

print("Total: {:.2f}".format(49))  #float format
print("Total: {:<8} Rs".format(49))  #Right
print("Total: {:>8} Rs".format(49))  #Left
print("Total: {:^8} Rs".format(49))  #Center
print("Total: {:=8} Rs".format(-49))
print("The Universe is {:,} Year Old".format(99999999999))
print("The Universe is {:_} Year Old".format(99999999999))
print("16 in Binary is {:b}".format(15))
print("1110 in Binary is {:d}".format(0b1110))
print("1110 in Binary is {:d}".format(0b1110))




# Program to Remove Duplicate in String with sorting
user_input = input("Enter the String with Duplicate Words = ")

result = " ".join(sorted(set(user_input.split(" "))))
print(result)
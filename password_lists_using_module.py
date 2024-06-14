# User Enters the Password & if Password Validate it Return in String Else Not
from password_validation_module import validate
print("Enter the Password Between 6-12 Digit, One Capital, One Small Case Letter, and Special "
                     "Character (#$%)\nps - Press C/c to Stop Entering for Password")
password_dictionary = {"accepted": [], "rejected": []}
while True:
    password = input()
    if password.lower() == 'c':
        break
    else:
        if validate(password):
            password_dictionary['accepted'].append(password)
        else:
            password_dictionary['rejected'].append(password)

print(password_dictionary)
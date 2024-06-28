# importing shutil module
import shutil

# search the file
cmd = "virtualenv"

# Using shutil.which() method
locating = shutil.which(cmd)

# Print result
print(locating)

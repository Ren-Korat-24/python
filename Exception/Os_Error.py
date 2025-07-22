# Importing os module
import os

# os.ttyname() method in Python is used to get the terminal 
# device associated with the specified file descriptor.
# and raises an exception if the specified file descriptor 
# is not associated with any terminal device.
print(os.ttyname(1))
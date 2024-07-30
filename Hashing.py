
import hashlib
import getpass

# Get the password from the user without echoing it to the console

# user_password = input("Password")
# This takes the password withut showing it on the console/terminal
user_password = getpass.getpass("Enter your password: ")
# Create a new hash object using a secure algorithm (e.g. SHA-256)
hasg_obj = hashlib.sha256()
# Update the hash object with the password bytes
hasg_obj.update(user_password.encode('utf-8'))

password_hash = hasg_obj.hexdigest()

print("Stored Hash :", password_hash)

input_pass = getpass.getpass("Enter your password again: ")
input_obj = hashlib.sha256()
input_obj.update(input_pass.encode('utf-8'))

confirm_hash = input_obj.hexdigest()

if password_hash == confirm_hash:
    print("Password is the same")
else:
    print("password is not the same or is incorrect")    







# Get the hexadecimal representation of the hash

# Print the stored hash (for testing purposes)

# Get the password from the user again for verification

# Hash the input password using the same algorithm as before

# Compare the stored hash with the input hash

# Check if the passwords match and print a success or failure message

# Import the necessary libraries for hashing and secure password input

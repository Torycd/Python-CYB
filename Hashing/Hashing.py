import hashlib
import getpass

def hashing(user_password):
    hasg_obj = hashlib.sha256()
    # Update the hash object with the password bytes
    hasg_obj.update(user_password.encode('utf-8'))
    password_hash = hasg_obj.hexdigest()

    return password_hash
    
def confirm_password(password_hash, input_password):

    input_hashing = hashing(input_password)
    return password_hash == input_hashing
        

def main():
    # This takes the password without showing it on the console/terminal
    user_password = getpass.getpass("Enter your password: ")
    password_hash = hashing(user_password)
    input_password = getpass.getpass("Enter your password again: ")
    if confirm_password(password_hash, input_password):
        print("Password is Correct")
        print(password_hash)
    else:
        print("Password is Not Correct!")


if __name__ == "__main__":
    main()

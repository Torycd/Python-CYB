# - Goal: Design a simple authentication system for a fictional website/application
# - Requirements:
#     - User registration:
#         - Take username, password, and email input
#         - Hash password using a secure algorithm (e.g., SHA-256)
#         - Store username, hashed password, and email in a database (e.g., CSV file)
#     - User login:
#         - Take username and password input
#         - Hash input password
#         - Compare hashed input password with stored hash in database
#         - Authenticate user if matches, otherwise reject

def Registration():
    username = input("Input username: ")
    password = input("Input password: ")
    email = input("Input email address: ")
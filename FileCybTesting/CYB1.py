with open("list.txt", "r") as file:
    file_text = file.read()
username = file_text.split()
# print(username)

def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter + 1
    if counter >= 3:
        return "you have tried to login three or more times. your account has been locked"
    else:
        return "You can login"

login_check(username, "Liam")
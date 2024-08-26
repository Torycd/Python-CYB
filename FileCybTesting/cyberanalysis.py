
with open("large_login_details.txt", "r") as file:
    file_text = file.read()

file_list = file_text.split()

status_list = []
username_list = []
password_list = []
no_list = []

for record in file_list:
    username, password, num_logins, status = record.split(',')
    username_list.append(username)
    password_list.append(password)
    no_list.append(int(num_logins))
    status_list.append(status)

def account_status():
    counter_locked = 0
    counter_unlocked = 0
    for state in status_list:
        if state == "locked":
            counter_locked += 1   
        elif state == "unlocked":
            counter_unlocked += 1
    print("No of locked account", counter_locked)
    print("No of locked account", counter_unlocked)

def account_login_attempts():
    counter_five_or_more = 0
    counter_four_or_less = 0
    for count in no_list:
        if count >= 5:
            counter_five_or_more += 1
        elif count < 5:
            counter_four_or_less += 1
    print(counter_five_or_more,"have attempted login more than 4 times")      
    print(counter_four_or_less,"have attempted login less than 5 times")      

def check_wrong_status():
    counter_unlocked = 0
    counter_locked = 0
    for num_logins, status in zip(no_list, status_list):
        if num_logins >= 5 and status == "unlocked":
            counter_unlocked += 1
        elif num_logins < 5 and status == "locked":
            counter_locked += 1
    print(counter_locked, "are wrongfully locked")        
    print(counter_unlocked, "should be locked")        

account_status()
account_login_attempts()
check_wrong_status()
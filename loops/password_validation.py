username = 'eric'

is_valid = False
while not is_valid:
    password = input('enter a password')
    # check if the password is valid, ask for another if not
    # valid passwords are at least 8 characters long, and do not
    # contain the username
    is_valid = len(password) >= 8 and not username in password


# another way to setup the loop:
password = input('enter a password')
while not(len(password) >= 8 and not username in password):
    print('passwords must be 8 or more characters  and must not contain the username!')
    password = input('enter a password')

file_in = open('./fileIO/names_and_passwords.txt', 'r')
file_out = open('./fileIO/names_and_passwords_hashed.txt', 'w')

for line in file_in:
    parts = line.strip().split(',')
    hashed_password = parts[1].__hash__()
    file_out.write(f'{parts[0]},{hashed_password}\n')

file_in.close()
file_out.close()


# now the user login part
file = open('./fileIO/names_and_passwords_hashed.txt', 'r')
authorized_users = file.read().split('\n')
file.close()

username = 'Juliet'  #input('enter username: ')
password = 'aRoseByAnyOtherName'  #input('enter password: ')
password_hash = password.__hash__()
credential = f'{username},{password_hash}'

for authorized_user in authorized_users:
    if credential == authorized_user:
        print('login successful')

def print_happy_bday() -> None:
    print('happy birthday to you')

def sing_happy_bday(name: str) -> None:
    print_happy_bday()
    print_happy_bday()
    print(f'happy birthday dear {name}')
    print_happy_bday()

user_name = input('enter your name: ')
sing_happy_bday(user_name)
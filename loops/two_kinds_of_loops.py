import random

# a simple guess-a-number program
secret_number = random.randint(1, 5)

guess = int(input("I'm thinking of a number between 1 and 5. Guess: "))

while guess != secret_number:
    print('wrong!')
    guess = int(input("I'm thinking of a number between 1 and 5. Guess: "))

print('right!')



# print each character in a string on its own line
my_string = "hello world!"
for ch in my_string:
    print(ch)


# for num in [1, 2, 3, 4, 5]:
#     print(num)

for num in range(0, 101):
    print(num)


for num in range(0, 10, 2):
    square = num ** 2
    print(f'the square of {num} is {square}')


string = 'hello world'
for index in range(len(string)):
    print(f'at index {index} is letter {string[index]}')
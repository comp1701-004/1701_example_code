def add_stuff() -> None:
    "this function adds the numbers 1 and 2 and prints the sum"
    x = 1
    y = 2
    the_sum = x + y
    print(f'{x} + {y} = {the_sum}')

def multiply_stuff() -> None:
    x = 3
    y = 4
    the_product = x * y
    print(f'{x} * {y} = {the_product}')

x = 5
y = 6
add_stuff()
multiply_stuff()
print(x, y)


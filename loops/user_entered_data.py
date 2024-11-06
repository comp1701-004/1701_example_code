is_done = False

while not is_done:
    price = float(input('enter a price: '))
    print(f'gst amount is {price * 0.05:.2f}')
    is_done = input('are you done entering prices? (y/n)') == 'y'



# here is a sentinel-loop version, where the user can enter
# a negative price to quit
price = float(input('enter a price (negative to quit): '))

while price >= 0:
    print(f'gst amount is {price * 0.05:.2f}')
    price = float(input('enter a price (negative to quit): '))

# here's another version of the sentinel loop
# note this one has weird behavior if the user enters a negative
# as the first number
price = 0
while price >= 0:
    price = float(input('enter a price: '))
    print(f'gst amount is {price * 0.05:.2f}')
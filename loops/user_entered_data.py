is_done = False

while not is_done:
    price = float(input('enter a price: '))
    print(f'gst amount is {price * 0.05:.2f}')
    is_done = input('are you done entering prices? (y/n)') == 'y'

for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
    for column in range(1, 11):
        print(f'{row}{column}')


for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
    for rank in range(0, 14):
        print(f'{rank} of {suit}')
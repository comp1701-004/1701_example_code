two_thirds = 2/3

print(f'10-characters wide in sci. notation: _{two_thirds:^.4%}_')


big_number = 10000000
print(f'a big number with comma-thousand-separators: {big_number:10,.2f}')


G = 6.6743e-11  # this is the gravitational constant (usually denoted "g")

# in scientific notation with 5-digits precision
print(f'{G:.5e}')

# as a float with 15 digits of precision
print(f'{G:.15f}')
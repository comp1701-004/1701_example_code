a=5
b=10
user_name = 'eric'

print(a > b)
print(type(user_name == 'eric'))

print(b < a)
print(not (b < a))


# XOR
a = False
b = True
xor = (a and not b) or (b and not a)
xor = a != b
print(xor)
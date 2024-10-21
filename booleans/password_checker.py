username = 'eric'
password = 'ericisthebest'

# print False if username is contained in password
# True otherwise
is_valid = not username in password

#another way:
is_valid = password.count(username) == 0

print(is_valid)


a = True
b = False
c = True
d = True

everything = a and b and c and d
anything = a or b or c or d
nothing = not a and not b and not c and not d
nothing = not anything

print(everything)


x = 20
# check if x is in the range of -10 to 5 (inclusive)
inside = (x <= 5) and (x >= -10)
inside = -10 <= x <= 5  # this is a python shorthand - no other languages support it (DONT USE IN THIS CLASS!)
print(inside)

# check if it's outside that range
outside = (x > 5) or (x < -10)
outside = not inside  # another way
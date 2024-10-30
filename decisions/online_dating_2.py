
def is_kind() -> bool:
    return input('are you kind? (y/n)') == 'y'

def smells_good() -> bool:
    return input('do you smell good? (y/n)') == 'y'

def is_loud() -> bool:
    return input('are you loud? (y/n)') == 'y'

def is_broke() -> bool:
    return input('are you broke? (y/n)') == 'y'


# result = 'no match'
# if is_kind() or smells_good():
#         if not is_loud():
#             if not is_broke():
#                 result = 'match'
# print(result)

# as a 1-liner
result = 'no match'
if (is_kind() or smells_good()) and not is_loud() and not is_broke:
    result = 'match'
print(result)



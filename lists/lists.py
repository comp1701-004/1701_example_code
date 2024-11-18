# strings are a sequence of characters
my_string = 'hello world'
print(my_string[1])

# create some lists that are sequences of strings
acceptable_flavours = ['vanilla', 'chocolate', 'Neapolitan', 'tiger', 'peppermint']
unacceptable_flavours = ['mint-chocolate']
empty_list = []

# lists of numeric or mixed data types
numbers = [1, 2, 3, 4, 5]
mixed = ['John Doe', 27, 1550.87]

# cast a range to a list
print(list(range(0, 10)))
print(list('hello world'))

# access individual things from the list by index
print(acceptable_flavours[0])

# modify by index
# my_string = 'hello world'
# my_string[0] = 'J' # this doesn't work b/c strings are immutable
acceptable_flavours[0] = 'rainbow'
print(acceptable_flavours)

# negative indexes
print(acceptable_flavours[-1], acceptable_flavours[-2])

# remove item by index
# print(acceptable_flavours)
# del acceptable_flavours[-1]
# print(acceptable_flavours)

# measure the len of a string, list, and range
print(len('hello world'))
print(len([2, 4, 6]))
print(len(range(100)))

# split and join methods
my_string = "chalmers,eric,6'3"
elements = my_string.split(',')
print(elements)
joined_string = ','.join(elements)
print(joined_string)

# append method
my_list = [1, 2, 4, 5]
my_list.append(6)
my_list.insert(2, 3)
print(my_list)

# + operator
print('hello ' + 'world')
print([1, 2, 3] + [4, 5, 6])

# in operator
print('mint chocolate' in acceptable_flavours)
print('peppermint' in acceptable_flavours)

# 2D list
couples = [
    ['angelina', 'brad'], 
    ['romeo', 'juliet'], 
    ['chocolate', 'peanut butter']
]

scores = [
    [84, 85, 86],
    [77, 78, 79],
    [92, 93, 94],  # student 2
    [20, 60, 100]
]
print(scores[0][2])

# print out all scores
for student_number in range(4):
    for assignment_number in range(3):
        print(
            f'score #{assignment_number} for student #{student_number} = {scores[student_number][assignment_number]}'
            )


days = ['Su', 'M', 'Tu', 'W', 'Tr', 'F', 'Sa']
days.reverse()
print(days)
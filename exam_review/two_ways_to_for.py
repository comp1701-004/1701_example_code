# write some code that will increase each item in a list by one
my_list = [2, 3, 4, 5]  # -> [3, 4, 5, 6]

# this doesn't work...
for item in my_list:
    item += 1 # because this line increments the "item" variable
              # not the original list
print(my_list)

# instead, access & increment the items in the list by index
for index in range(len(my_list)):
    my_list[index] += 1
print(my_list)

# if you need to modify the list contents, or know where in the 
# list each item resides, for-loop by index.
# otherwise for looping through values is probably easiest


# another situation
# say you need to locate where in a list a particular value is
my_list = ['a', 'b', 'd', 'g', 'z']
# what is the index of the letter "d"?

# this allows us to confirm that "d" is in the list
# but we have no way to identify where
for item in my_list:
    item == 'd'

# this works better for this case
index_of_d = -1
for index in range(len(my_list)):
    if item == 'd':
        index_of_d = index


# another example from lab 8
# remove courses with a particular code
courses = ["COMP 1501", "GNED 1103", "GNED 1401", "MATH 1505"]
# must loop by index so we can delete courses at the appropriate indices
# can't loop through forwards, because then as we delete,
# we remove higher indexes.
for index in range(len(courses)-1, -1, -1): 
    parts = courses[index].split(' ')
    if parts[0] == 'GNED':
        del courses[index]
print(courses)


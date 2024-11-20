numbers = [10,20,30,40,50]

# this doesn't work b/c the "number" variable is being
# modified, not the original list
for number in numbers:
    number += 1
print(numbers)

# instead, lets loop through indexes and modify list
# contents by index
for index in range(len(numbers)):
    numbers[index] += 1
print(numbers)

# here's the same loop as a while loop
# (just for fun - the for loop is actually the right tool here)
index = 0
while index < len(numbers):
    numbers[index] += 1
    index += 1
print(numbers)
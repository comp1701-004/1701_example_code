# write some text to a file
file = open('./fileIO/diary.txt', 'w')

file.write('Dear diary,\n')
file.write('Today I aced assignment 4')

file.close()

# open it back up in read mode
file = open('./fileIO/diary.txt', 'r')
contents = file.read()
file.close()
print(contents)


# now do it line-by-line with readline()
file = open('./fileIO/diary.txt', 'r')
print(file.readline())
print(file.readline())
file.close()


# now do it line-by-line with a for loop()
file = open('./fileIO/diary.txt', 'r')
for line in file:
    print(line)
file.close()


# finally, read all lines into a list using readlines()
file = open('./fileIO/diary.txt', 'r')
lines = file.readlines()
file.close()
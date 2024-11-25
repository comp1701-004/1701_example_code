file_in = open('./fileIO/payments.txt', 'r')
file_out = open('./fileIO/payments_doctored.txt', 'w')

for line in file_in:
    line_parts = line.split(' ')
    # if N.Korea is the last thing in the list don't add it
    # in other words, if N.Korea is not the last thing, do add it
    if 'N.Korea' != line_parts[-1].strip():
        file_out.write(line)

file_in.close()
file_out.close()
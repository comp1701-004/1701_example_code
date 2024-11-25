file = open('./fileIO/payments.txt', 'r')
total = 0

for line in file:
    # the line will look something like: '$12000 2022-01-15 Canada'
    line_parts = line.split(' ')
    dollar_amt_str = line_parts[0][1:]
    dollar_amt_int = int(dollar_amt_str)
    total += dollar_amt_int

file.close()
print(total)
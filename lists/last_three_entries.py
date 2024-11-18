entry = input('enter some text, enter to quit: ')
entries = []

while entry != '':

    # process the input by adding it to a list
    # only keep last 3 entries
    entries.append(entry)

    if len(entries) > 3:
        del entries[0]
    
    print(entries)

    entry = input('enter some text, enter to quit: ')

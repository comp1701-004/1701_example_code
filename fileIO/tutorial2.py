
file = open('./fileIO/import_this.txt', 'r')

lines = file.read().split('\n')
file.close()

# count number of lines
print(f'# of lines {len(lines)}')

# build a list of all words
words = []
for line in lines:
    words = words + line.split(' ')
print(f'# of words = {len(words)}')

# remove stopwords
file = open('./fileIO/stop_words.txt', 'r')
stop_words = file.read().lower().split('\n')
file.close()

keep_words = []
for word in words:
    if word.lower() not in stop_words:
        keep_words.append(word)
print(f'# of words without stopwords: {len(keep_words)}')

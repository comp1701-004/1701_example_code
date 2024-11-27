import this
import os

text = input('enter some text: ')
all_text = []

while text != '':
    all_text.append(text)
    text = input('enter some text: ')

print(f'{len(all_text)} lines of text written')

# check if the file already exists
file_exists = os.path.isfile('./fileIO/tutorial1.txt')

file = open('./fileIO/tutorial1.txt', 'a')
if file_exists:
    file.write('\n\n')
file.write('\n'.join(all_text))

file.close()
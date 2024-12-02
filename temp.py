def count_words(text: str, stopwords: list) -> int:
    "count the words in text, excluding any words in the stopwords list"
    
    words = text.split(' ')

    for word in words:
        word_count = 0
        if word.lower() not in stopwords:
            word_count += 1
    
    return word_count


def main() -> None:
    "read the text in a file, count the number of words not in a list of stop words"
    
    stopwords = ['am', 'the', 'you']
    file = open('text.txt', 'r')
    word_count = 0
    
    text_lines = file.read().split('\n')
    for line in text_lines:
        word_count += count_words(line)

    print(word_count)



total_pennies = 125
people = 3

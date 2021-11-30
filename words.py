def print_upper_words(words, letters):
    """ print al the words in the words list in capitalized """
    for word in words:
        for letter in letters:
            if word[0] == letter:
                print(word.upper())
                break
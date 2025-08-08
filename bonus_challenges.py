def count_word_frequency(filename):
    import string
    word_count = {}
    with open(filename, 'r') as file:
        text = file.read().lower()
        for char in string.punctuation:
            text = text.replace(char, '')
        words = text.split()
        for  word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    result = count_word_frequency('sample.txt')
    print(result)                
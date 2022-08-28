import re
from hashtable import Hashtable

def repeated_word(phrase: str):
    # In Plain English:
    # Split phrase into individual words.
    # Check if hash table contains next word.
    # If word already in hash table, return word.
    # If not, put word in hash table
    # Go to next word and check if in hash table.

    # Algorithm:
    # 1. Split phrase
    # 2. Loop over words
    # 2a. Check hash table for word
    # 2b. If true, return word
    # 2c. If not, add word to table

    list_of_words = re.split(r' |,|;|\.|\?|!|:|-', phrase.lower())
    print(list_of_words)

    hashtable_of_words = Hashtable()

    for word in list_of_words:
        if hashtable_of_words.contains(word):
            return word
        hashtable_of_words.set(word, word)

        print(hashtable_of_words.keys())


if __name__ == '__main__':
    print(repeated_word("It was the best of times, it was the worst of times."))


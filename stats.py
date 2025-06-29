from collections import Counter

def book_text_number (book_text):
    num_words = book_text.split()
    return len(num_words)

def book_character_occurences (book_text):
    return Counter(char.lower() for char in book_text)

def book_text_number (book_text):
    num_words = book_text.split()
    return len(num_words)

def book_character_occurences (book_text):
    characters = list(book_text)
    char_dict = {}
    for char in characters:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1

    return char_dict

from collections import Counter

def count_words (book_text):
    num_words = book_text.split()
    return len(num_words)

def character_frequencies (book_text):
    characters = list(book_text)
    char_dict = {}
    for char in characters:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1

    return char_dict

def frequency_sort (book_occurences):
    list_occurences = book_occurences.items()
    sorted_by_frequency = sorted(list_occurences, key=lambda x: x[1], reverse=True)
    lists = [occ for occ in sorted_by_frequency if occ[0].isalpha()]
    return lists
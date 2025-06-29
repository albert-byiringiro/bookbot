from stats import book_text_number, book_character_occurences

def get_book_text (path_to_file):
    with open(path_to_file, 'r') as file:
        file_contents = file.read()
    return file_contents

def main ():
    book_text = get_book_text('./books/frankenstein.txt')
    num_words = book_text_number(book_text)
    # print(f"{num_words} words found in the document")
    print(book_character_occurences(book_text))


main()
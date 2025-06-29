def get_book_text (path_to_file):
    with open(path_to_file, 'r') as file:
        file_contents = file.read()
    return file_contents

def book_text_number (book_text):
    num_words = book_text.split()
    return len(num_words)

def main ():
    book_text = get_book_text('./books/frankenstein.txt')
    num_words = book_text_number(book_text)
    print(f"{num_words} words found in the document")


main()
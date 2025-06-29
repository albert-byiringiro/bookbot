def get_book_text (path_to_file):
    with open(path_to_file, 'r') as file:
        file_contents = file.read()
    return file_contents


def main ():
    print(get_book_text('./books/frankenstein.txt'))


main()
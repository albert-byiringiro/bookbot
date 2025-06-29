from stats import frequency_sort, count_words, character_frequencies

def get_book_text (path_to_file):
    with open(path_to_file, 'r') as file:
        file_contents = file.read()
    return file_contents

def main ():
    print("============ BOOKBOT ============")

    book_text = get_book_text('./books/frankenstein.txt')
    print("Analyzing book found at books/frankenstein.txt...")
    
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    book_occurences = character_frequencies(book_text)
    sorted_counts = frequency_sort(book_occurences)
    for char, count in sorted_counts:
        print(f"{char}: {count}")
    
    print("============= END ===============")


main()
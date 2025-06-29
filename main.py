import sys
from stats import frequency_sort, count_words, character_frequencies

def get_book_text (path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        book_text = get_book_text(sys.argv[1])
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found.")
        sys.exit(1)

    print(f"Analyzing book found at {sys.argv[1]}...")
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
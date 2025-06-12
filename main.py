from stats import get_num_words, get_num_characters, create_list_from_dict
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    file_location = sys.argv[1]
    file_as_string = get_book_text(file_location)
    num_words = get_num_words(file_as_string)
    num_char_dict = get_num_characters(file_as_string)
    list_of_chars = create_list_from_dict(num_char_dict)
    report = f'''============ BOOKBOT ============
Analyzing book found at {file_location}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
'''
    for dict in list_of_chars:
        if dict['char'].isalpha():
            report += f"{dict['char']}: {dict['num']}\n"
        
    print(report)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

main()
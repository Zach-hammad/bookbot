from stats import count_word, count_char, sort_dict
import sys

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        num_words = count_word(get_book_text(sys.argv[1]))
        print(f"{" BOOKBOT ":=^31}")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print(f"{" Word Count ":-^31}")
        print(f"Found {num_words} total words") 
        print(f"{" Character Count ":-^31}")
        num_char = count_char(get_book_text(sys.argv[1]))
        sorted_dict = sort_dict(num_char)
        for i in sorted_dict: 
            print(f"{i["char"]}: {i["num"]}")
        print(f"{" END ":=^31}")
        sys.exit(0)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()


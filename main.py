from stats import count_word, count_char, sort_dict

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = count_word(get_book_text("books/frankenstein.txt"))
    print(f"{" BOOKBOT ":=^31}")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"{" Word Count ":-^31}")
    print(f"Found {num_words} total words")
    print(f"{" Character Count ":-^31}")
    num_char = count_char(get_book_text("books/frankenstein.txt"))
    sorted_dict = sort_dict(num_char)
    for i in sorted_dict:
        print(f"{i["char"]}: {i["num"]}")
    print(f"{" END ":=^31}")
main()


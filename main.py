def count_word(words):
    lst = words.split()
    return len(lst)

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = count_word(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()


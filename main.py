def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f"{num_words} words found in the document")
    print(char_count)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text_dict = {}
    for c in text.lower():
        text_dict[c] = text_dict.get(c,0) + 1
    return text_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

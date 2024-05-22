def read_book(book):
    with open(f"books/{book}", "r") as f:
        return f.read()


def count_letters(book):
    letters = {}
    for character in book.lower():
        if character not in letters.keys():
            letters[character] = 1
        else:
            letters[character] += 1
    return letters


def count_words(book):
    return len(book.split())


def main():
    title = "frankenstein.txt"
    book = read_book(title)
    print(f"{title} contains {count_words(book)} words!")
    print(count_letters(book))


if __name__ == "__main__":
    main()

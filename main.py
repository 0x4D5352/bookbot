def read_book(book):
    with open(f"books/{book}", "r") as f:
        return f.read()


def count_words(book):
    return len(book.split())

def main():
    book = "frankenstein.txt"
    print(read_book(book))


if __name__ == "__main__":
    main()

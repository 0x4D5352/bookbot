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


def sort_counts(letters):
    letters_list = []
    for letter, count in letters.items():
        letters_list.append({"letter": letter, "count": count})

    sort_on_count = lambda dict: dict["count"]

    letters_list.sort(reverse=True, key=sort_on_count)
    return letters_list


def main():
    title = "frankenstein.txt"
    book = read_book(title)
    print(f"--- begin report of {title} ---")
    print(f"{title} contains {count_words(book)} words!\n")
    for letter in sort_counts(count_letters(book)):
        if letter["letter"].isalpha():
            print(f"the {letter["letter"]} character was found {letter["count"]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()

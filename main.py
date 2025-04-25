import sys
from stats import count_words

def read_book(book):
    with open(book, "r") as f:
        return f.read()


def count_letters(book):
    letters = {}
    for character in book.lower():
        if character not in letters.keys():
            letters[character] = 1
        else:
            letters[character] += 1
    return letters




def sort_counts(letters):
    letters_list = []
    for letter, count in letters.items():
        letters_list.append({"letter": letter, "count": count})

    sort_on_count = lambda dict: dict["count"]

    letters_list.sort(reverse=True, key=sort_on_count)
    return letters_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    title = sys.argv[1]
    book = read_book(title)
    print(f"--- begin report of {title} ---")
    # print(f"{count_words(book)} words found in the document\n")
    print(f"{title} contains {count_words(book)} words!\n")
    for letter in sort_counts(count_letters(book)):
        if letter["letter"].isalpha():
            print(f"{letter["letter"]}: {letter["count"]}")
            # print(f"the {letter["letter"]} character was found {letter["count"]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()

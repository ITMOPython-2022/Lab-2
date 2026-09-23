import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


BASE_DIR = Path(__file__).parent
BOOKS_PATH = BASE_DIR / "books-en.csv"
CURRENCY_PATH = BASE_DIR / "currency.xml"
BIBLIOGRAPHY_PATH = BASE_DIR / "bibliography.txt"

YEAR_LIMIT = 2000
SEARCH_LIMIT = 10


def read_books():
    with BOOKS_PATH.open(encoding="windows-1251", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def get_year(book):
    try:
        return int(book["Year-Of-Publication"])
    except ValueError:
        return 0


def filtered_books(books):
    return [book for book in books if get_year(book) >= YEAR_LIMIT]


def count_long_titles(books):
    return sum(1 for book in books if len(book["Book-Title"]) > 30)


def search_by_author(books, author_query, limit=SEARCH_LIMIT):
    query = author_query.lower()
    found_books = [
        book
        for book in filtered_books(books)
        if query in book["Book-Author"].lower()
    ]
    return found_books[:limit]


def make_bibliography(books, amount=20):
    chosen_books = filtered_books(books)[:amount]

    with BIBLIOGRAPHY_PATH.open("w", encoding="utf-8") as file:
        for number, book in enumerate(chosen_books, start=1):
            author = book["Book-Author"]
            title = book["Book-Title"]
            year = book["Year-Of-Publication"]
            file.write(f"{number}. {author}. {title} - {year}\n")

    return BIBLIOGRAPHY_PATH


def currency_name_to_char_code():
    tree = ET.parse(CURRENCY_PATH)
    root = tree.getroot()
    result = {}

    for valute in root.findall("Valute"):
        name = valute.findtext("Name")
        char_code = valute.findtext("CharCode")
        result[name] = char_code

    return result


def unique_publishers(books):
    return sorted({book["Publisher"] for book in books if book["Publisher"]})


def top_books(books, amount=20):
    return sorted(
        books,
        key=lambda book: int(book["Downloads"] or 0),
        reverse=True,
    )[:amount]


def print_search_results(found_books):
    print(f"Search results, limited to {SEARCH_LIMIT}:")
    if not found_books:
        print("No books found.")
        return

    for number, book in enumerate(found_books, start=1):
        print(
            f"{number}. {book['Book-Author']}. "
            f"{book['Book-Title']} - {book['Year-Of-Publication']}"
        )


def main():
    books = read_books()
    author_query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Rowling"

    print("Lab 2. Variant 10")
    print(f"Books file: {BOOKS_PATH.name}")
    print(f"Books with title longer than 30 symbols: {count_long_titles(books)}")
    print()

    print_search_results(search_by_author(books, author_query))
    print()

    bibliography_path = make_bibliography(books)
    print(f"Bibliography saved to {bibliography_path.name}")
    print()

    currency_dictionary = currency_name_to_char_code()
    print('Currency dictionary "Name - CharCode":')
    for name, char_code in currency_dictionary.items():
        print(f"{name}: {char_code}")
    print()

    publishers = unique_publishers(books)
    print(f"Unique publishers count: {len(publishers)}")
    print("First 20 unique publishers:")
    for publisher in publishers[:20]:
        print(f"- {publisher}")
    print()

    print("Top 20 books by downloads:")
    for number, book in enumerate(top_books(books), start=1):
        print(
            f"{number}. {book['Book-Title']} "
            f"({book['Downloads']} downloads)"
        )


if __name__ == "__main__":
    main()

def insertion_sort(books):
    for i in range(1, len(books)):
        key = books[i]
        j = i - 1
        while j >= 0 and key['year'] < books[j]['year']:
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key
    return books


books = [
    {"title": "To Kill a Mockingbird", "year": 1960},
    {"title": "Pride and Prejudice", "year": 1813},
    {"title": "1984", "year": 1949},
    {"title": "The Great Gatsby", "year": 1925},
    {"title": "The Catcher in the Rye", "year": 1951}
]

print("Original order:")
for book in books:
    print(f"{book['title']} ({book['year']})")

sorted_books = insertion_sort(books)

print("\nSorted by year:")
for book in sorted_books:
    print(f"{book['title']} ({book['year']})")

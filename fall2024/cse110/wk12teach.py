class Book:
    def __init__(self, scripture, book, chapters):
        self.scripture = scripture
        self.book = book
        self.chapters = chapters

formattedBooks = []

choice = input("Which volume of scripture would you like to learn about? ")

with open('books_and_chapters.txt') as books:
    for book in books:
        splitBook = book.split(':')
        formattedBooks.append(Book(splitBook[2].strip(), splitBook[0].strip(), int(splitBook[1].strip())))

largestBook = Book('','',0)

for book in formattedBooks:
    if book.scripture.lower() == choice.lower():
        print(f'Scripture: {book.scripture}, Book: {book.book}, Chapters: {book.chapters}')
        if book.chapters>largestBook.chapters:
            largestBook = book

print(f'The book with the most chapters in {choice} is {largestBook.book} in {largestBook.scripture} with {largestBook.chapters} chapters')
class Book:
    def __init__(self, title, author):
        self.title = title                # public
        self.author = author              # public
        self._is_checked_out = False      # private-like attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find the book by title and check it out."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return

    def return_book(self, title):
        """Find the book by title and return it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Print all books that are available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

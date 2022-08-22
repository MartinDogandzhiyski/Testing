from unittest import TestCase, main

from project.bookstore import Bookstore

class BookstoreTests(TestCase):
    def test_init(self):
        bookstore = Bookstore(3)
        self.assertEqual(bookstore.books_limit, 3)
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(bookstore._Bookstore__total_sold_books, 0)

    def test_total_sold_books_property(self):
        bookstore = Bookstore(3)
        self.assertEqual(bookstore.total_sold_books, 0)
        self.assertEqual(bookstore.total_sold_books, bookstore._Bookstore__total_sold_books)

    def test_book_limit_if_raises(self):
        with self.assertRaises(ValueError) as ex:
            bookstore = Bookstore(0)
        self.assertEqual(f"Books limit of 0 is not valid", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            bookstore = Bookstore(-2)
        self.assertEqual(f"Books limit of -2 is not valid", str(ex.exception))

    def test_len_method_if_works_properly(self):
        bookstore = Bookstore(5)
        bookstore.availability_in_store_by_book_titles = {"aa": 2, "bb": 3}
        result = bookstore.__len__()
        self.assertEqual(5, result)

    def test_receive_book_if_raises(self):
        bookstore = Bookstore(6)
        bookstore.availability_in_store_by_book_titles = {"aa": 2, "bb": 3}
        with self.assertRaises(Exception) as ex:
            bookstore.receive_book('rrr', 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual(5, bookstore.__len__())
        self.assertEqual(bookstore.total_sold_books, 0)

    def test_if_book_title_in_bookstore_and_not(self):
        bookstore = Bookstore(7)
        bookstore.availability_in_store_by_book_titles = {"aa": 2, "bb": 3}
        result = bookstore.receive_book('rrr', 1)
        self.assertEqual({"aa": 2, "bb": 3, 'rrr': 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(result, f"1 copies of rrr are available in the bookstore.")
        self.assertEqual(6, bookstore.__len__())
        self.assertEqual(bookstore.total_sold_books, 0)
        bookstore_one = Bookstore(7)
        bookstore_one.availability_in_store_by_book_titles = {"aa": 2, "bb": 3}
        result = bookstore_one.receive_book('bb', 1)
        self.assertEqual(6, bookstore.__len__())
        self.assertEqual({"aa": 2, "bb": 4}, bookstore_one.availability_in_store_by_book_titles)
        self.assertEqual(result, f"4 copies of bb are available in the bookstore.")
        self.assertEqual(bookstore.total_sold_books, 0)

    def test_sell_book_if_raises_with_no_book(self):
        bookstore = Bookstore(7)
        bookstore.availability_in_store_by_book_titles = {"aa": 2, "bb": 3}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book('ddd', 2)
        self.assertEqual(f"Book ddd doesn't exist!", str(ex.exception))
        self.assertEqual({"aa": 2, "bb": 3}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(bookstore.__len__(), 5)

    def test_sell_book_if_raises_with_more_books(self):
        bookstore = Bookstore(7)
        bookstore.availability_in_store_by_book_titles = {"aa": 2, "bb": 3}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book('aa', 5)
        self.assertEqual(f"aa has not enough copies to sell. Left: 2", str(ex.exception))
        self.assertEqual({"aa": 2, "bb": 3}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(bookstore.__len__(), 5)


    def test_sell_book_with_correct_data(self):
        bookstore = Bookstore(7)
        bookstore.availability_in_store_by_book_titles = {"aa": 2, "bb": 3}
        result = bookstore.sell_book('aa', 1)
        self.assertEqual({"aa": 1, "bb": 3}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(bookstore._Bookstore__total_sold_books, 1)
        self.assertEqual(bookstore.total_sold_books, 1)
        self.assertEqual(result, f"Sold 1 copies of aa")
        self.assertEqual(4, bookstore.__len__())
        result = bookstore.sell_book('aa', 1)
        self.assertEqual({"aa": 0, "bb": 3}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(bookstore._Bookstore__total_sold_books, 2)
        self.assertEqual(bookstore.total_sold_books, 2)
        self.assertEqual(result, f"Sold 1 copies of aa")
        self.assertEqual(3, bookstore.__len__())

    def test_str_method(self):
        bookstore = Bookstore(7)
        bookstore.receive_book('aa', 2)
        bookstore.receive_book('bb', 3)
        bookstore.sell_book('aa', 1)
        result = f"Total sold books: 1\n"
        result += f'Current availability: 4\n'
        result += f" - aa: 1 copies\n"
        result += f" - bb: 3 copies"
        self.assertEqual(result, bookstore.__str__())
        bookstore_one = Bookstore(7)
        result = f"Total sold books: 0\n"
        result += f'Current availability: 0'
        self.assertEqual(result, bookstore_one.__str__())




if __name__ == "__main__":
    main()
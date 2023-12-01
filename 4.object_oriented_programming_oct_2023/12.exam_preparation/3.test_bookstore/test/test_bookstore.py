# from project.bookstore import Bookstore
# from unittest import TestCase, main
#
#
# class TestGunitSquad(TestCase):
#
#     def setUp(self) -> None:
#         self.bookstore = Bookstore(10)
#         self.books = {"Python": 4, "R": 3}
#
#     def test_successful_initial(self):
#         self.assertEqual(10, self.bookstore.books_limit)
#         self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
#         self.assertEqual(0, self.bookstore.total_sold_books)
#         self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)
#
#     def test_unsuccessful_books_limit_setter_zero_or_negative_raise_value_error(self):
#         with self.assertRaises(ValueError) as ve:
#             self.bookstore.books_limit = 0
#
#         self.assertEqual("Books limit of 0 is not valid", str(ve.exception))
#
#     def test_successful__len__return_values_from_dict(self):
#         self.bookstore.availability_in_store_by_book_titles = self.books
#         result = len(self.bookstore)
#
#         self.assertEqual(7, result)
#         self.assertEqual(7, sum(self.bookstore.availability_in_store_by_book_titles.values()))
#
#     def test_unsuccessful_receive_book_raise_exception_book_limit(self):
#         self.bookstore.availability_in_store_by_book_titles = self.books
#         with self.assertRaises(Exception) as ex:
#             self.bookstore.receive_book("Python", 11)
#
#         self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
#         self.assertTrue(7 + 11 > self.bookstore.books_limit)
#
#     def test_successful_receive_book(self):
#         self.bookstore.availability_in_store_by_book_titles = {"R": 1}
#         self.assertEqual({"R": 1}, self.bookstore.availability_in_store_by_book_titles)
#         result = self.bookstore.receive_book("Python", 1)
#
#         self.assertEqual("1 copies of Python are available in the bookstore.", result)
#         self.assertEqual({"R": 1, "Python": 1}, self.bookstore.availability_in_store_by_book_titles)
#         self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["Python"])
#         result = self.bookstore.receive_book("Python", 1)
#         self.assertEqual("2 copies of Python are available in the bookstore.", result)
#         self.assertEqual({"R": 1, "Python": 2}, self.bookstore.availability_in_store_by_book_titles)
#         self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles["Python"])
#
#     def test_unsuccessful_sell_book_raise_exception_book_not_found(self):
#         with self.assertRaises(Exception) as ex:
#             self.bookstore.sell_book("C--", 3)
#
#         self.assertEqual("Book C-- doesn't exist!", str(ex.exception))
#         self.assertTrue("C--" not in self.bookstore.availability_in_store_by_book_titles)
#
#     def test_unsuccessful_sell_book_raise_exception_not_enough_copies(self):
#         self.bookstore.availability_in_store_by_book_titles = {"R": 1, "Python": 1}
#         with self.assertRaises(Exception) as ex:
#             self.bookstore.sell_book("R", 2)
#
#         self.assertEqual(f"R has not enough copies to sell. Left: 1", str(ex.exception))
#         self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["R"])
#         self.assertTrue(2 > self.bookstore.availability_in_store_by_book_titles["R"])
#
#         with self.assertRaises(Exception) as ex:
#             self.bookstore.sell_book("Python", 2)
#
#         self.assertEqual(f"Python has not enough copies to sell. Left: 1", str(ex.exception))
#         self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["Python"])
#         self.assertTrue(2 > self.bookstore.availability_in_store_by_book_titles["Python"])
#
#
#
#     def test_successful_sell_book(self):
#         self.bookstore.availability_in_store_by_book_titles = {"R": 2, "Python": 0}
#         result = self.bookstore.sell_book("R", 1)
#
#         self.assertEqual("Sold 1 copies of R", result)
#         self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["R"])
#         self.assertEqual(1, self.bookstore.total_sold_books)
#         self.assertEqual(1, self.bookstore._Bookstore__total_sold_books)
#
#         result = self.bookstore.sell_book("R", 1)
#         self.assertEqual("Sold 1 copies of R", result)
#         self.assertEqual(0, self.bookstore.availability_in_store_by_book_titles["R"])
#         self.assertEqual(2, self.bookstore.total_sold_books)
#         self.assertEqual(2, self.bookstore._Bookstore__total_sold_books)
#
#     def test__str__(self):
#         self.bookstore.availability_in_store_by_book_titles = {"R": 2, "Python": 0}
#         self.bookstore.sell_book("R", 1)
#         result = str(self.bookstore)
#
#         self.assertEqual("Total sold books: 1\n"
#                          "Current availability: 1\n"
#                          " - R: 1 copies\n"
#                          " - Python: 0 copies", result)
#
#
# if __name__ == "__main__":
#     main()


from project.bookstore import Bookstore
from unittest import TestCase, main


class TestGunit(TestCase):
    def setUp(self) -> None:
        self.book_store = Bookstore(10)

    def test_init(self):
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(10, self.book_store.books_limit)
        self.assertEqual(self.book_store.total_sold_books, self.book_store._Bookstore__total_sold_books)
        self.assertEqual(self.books_limit.total_sold_books, self.book_store.__books_limit)
        self.assertEqual(0, self.book_store._Bookstore__total_sold_books)

    def test_setter_books_limit(self):
        with self.assertRaises(ValueError) as error:
            store = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(error.exception))

    def test_count_the_total_number_of_books(self):
        self.book_store.availability_in_store_by_book_titles = {
            "Time": 3, "Space": 7
        }
        self.assertEqual(10, len(self.book_store))

    def test_receive_book_no_space(self):
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book("Hitler", 100)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_have_space(self):
        self.book_store.availability_in_store_by_book_titles ={"Top Gun": 3}
        result = self.book_store.receive_book("Maveric", 5)
        self.assertEqual("5 copies of Maveric are available in the bookstore.", result)
        self.assertEqual(2, len(self.book_store.availability_in_store_by_book_titles))

        result = self.book_store.receive_book("Maveric", 1)
        self.assertEqual("6 copies of Maveric are available in the bookstore.", result)
        self.assertEqual(2, len(self.book_store.availability_in_store_by_book_titles))



    def test_sell_book_not_available_in_store(self):
        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("Nqma", 1)

        self.assertEqual("Book Nqma doesn't exist!", str(error.exception))

    def test_sell_book_not_enough_copies(self):
        self.book_store.receive_book("Maveric", 5)

        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("Maveric", 6)

        self.assertEqual("Maveric has not enough copies to sell. Left: 5", str(error.exception))

    def test_sell_book(self):
        sold_book = ("Maveric", 5)
        sold_book1 = ("Test", 1)
        self.book_store.receive_book(*sold_book)
        self.book_store.receive_book(*sold_book1)
        self.book_store.receive_book("Test2", 1)

        self.assertEqual("Sold 5 copies of Maveric", self.book_store.sell_book(*sold_book))
        self.assertEqual(5, self.book_store.total_sold_books)
        self.assertEqual("Sold 1 copies of Test", self.book_store.sell_book(*sold_book1))
        self.assertEqual(6, self.book_store.total_sold_books)

    def test_str_output(self):
        sold_book = ("Maveric", 5)
        sold_book1 = ("Test", 1)
        sold_book2 = ("Test1", 4)
        self.book_store.receive_book(*sold_book)
        self.book_store.receive_book(*sold_book1)
        self.book_store.receive_book(*sold_book2)
        self.book_store.sell_book(*sold_book)

        self.assertEqual("Total sold books: 5\n"
                         "Current availability: 5\n"
                         " - Maveric: 0 copies\n"
                         " - Test: 1 copies\n"
                         " - Test1: 4 copies", str(self.book_store))


if __name__ == '__main__':
    main()

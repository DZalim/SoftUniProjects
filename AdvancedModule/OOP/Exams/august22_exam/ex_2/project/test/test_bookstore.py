from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self):
        self.bookstore = Bookstore(10)

    def test_correct_initialization(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_raises_error(self):

        expected_message = "Books limit of 0 is not valid"

        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual(expected_message, str(ve.exception))

    def test__len__method(self):
        self.bookstore.availability_in_store_by_book_titles = {'A': 2, 'B': 3, 'C': 4}
        self.assertEqual(9, self.bookstore.__len__())

    def test_receive_book_if_there_is_not_enough_space_in_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {'A': 2, 'B': 3, 'C': 4}
        expected_result = "Books limit is reached. Cannot receive more books!"

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('D', 5)

        self.assertEqual(expected_result, str(ex.exception))

    def test_receive_book_if_there_is_enough_space_in_bookstore_when_book_is_not_available(self):
        result = self.bookstore.receive_book('D', 5)
        expected_result = "5 copies of D are available in the bookstore."
        self.assertEqual(expected_result, result)

    def test_receive_book_if_there_is_enough_space_in_bookstore_when_book_is_available(self):
        self.bookstore.availability_in_store_by_book_titles = {'D': 4}

        result = self.bookstore.receive_book('D', 5)
        expected_result = "9 copies of D are available in the bookstore."
        self.assertEqual(expected_result, result)

    def test_sell_book_if_the_book_is_not_available_in_bookstore(self):
        expected_result = "Book A doesn't exist!"

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('A', 3)

        self.assertEqual(expected_result, str(ex.exception))

    def test_sell_book_if_there_is_not_enough_copies_of_that_book(self):
        self.bookstore.availability_in_store_by_book_titles = {'A': 4}

        expected_result = "A has not enough copies to sell. Left: 4"

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('A', 5)

        self.assertEqual(expected_result, str(ex.exception))

    def test_sell_book_correct(self):
        self.bookstore.availability_in_store_by_book_titles = {'A': 4}
        result = self.bookstore.sell_book('A', 3)
        expected_result = "Sold 3 copies of A"

        self.assertEqual(expected_result, result)
        self.assertEqual({'A': 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, self.bookstore.total_sold_books)

    def test__str__method(self):
        self.bookstore.availability_in_store_by_book_titles = {'A': 2, 'B': 3, 'C': 4}
        self.bookstore.sell_book('A', 1)

        expected_result = ["Total sold books: 1",
                  'Current availability: 8',
                  " - A: 1 copies", " - B: 3 copies", " - C: 4 copies"]

        self.assertEqual('\n'.join(expected_result), str(self.bookstore))


if __name__ == "__main__":
    main()

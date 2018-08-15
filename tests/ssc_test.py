import unittest
import os.path
import sys

# Just adding the bookssorter directory path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + '/sources')

import booksorter as bs
import config as c


def get_id2(books_list):
    id_list = []
    return [id_list.append(book['id']) for book in books_list]


def get_id(sorted_books_list):
    ids_list = []
    for book in sorted_books_list:
        ids_list.append(book['id'])
    return ids_list


class BooksSorterTest(unittest.TestCase):

    def test_title_ascending(self):
        rules = [['title', c.ASCENDING]]
        book_sorter = bs.BookSorter()
        books_test = book_sorter.sort_books(c.books_list, rules)
        myresult = get_id(books_test)
        self.assertEqual(c.result['a'], myresult)

    def test_author_ascending_title_descending(self):
        rules = [['title', c.DESCENDING], ['author', c.ASCENDING]]
        book_sorter = bs.BookSorter()
        books_test = book_sorter.sort_books(c.books_list, rules)
        myresult = get_id(books_test)
        self.assertEqual(c.result['b'], myresult)

    def test_edition_descending_author_descending_title_ascending(self):
        rules = [['author', c.DESCENDING], ['title', c.ASCENDING], ['edition_year', c.DESCENDING]]
        book_sorter = bs.BookSorter()
        books_test = book_sorter.sort_books(c.books_list, rules)
        myresult = get_id(books_test)
        self.assertEqual(c.result['c'], myresult)

    def test_null(self):
        rules = None
        book_sorter = bs.BookSorter()
        self.assertRaises(bs.SortingServiceException, book_sorter.sort_books, c.books_list, rules)

    def test_empty_set(self):
        rules = []
        book_sorter = bs.BookSorter()
        books_test = book_sorter.sort_books(c.books_list, rules)
        myresult = get_id(books_test)
        self.assertEqual(c.result['e'], myresult)


if __name__ == '__main__':
    unittest.main()

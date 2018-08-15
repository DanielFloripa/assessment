from sortingservice import Sorting


class BookSorter:

    @staticmethod
    def sort_books(books, rules):
        """
        Call the sortingService module
        :param books: Books to be sorted
        :param rules: Ascending or Descending rules
        :return: It returns a list of books sorted
        :Exceptions: when the order is null
        """

        if rules is None:
            raise SortingServiceException
        return Sorting.execute(books, rules)


class SortingServiceException(Exception):
        """
        An Exception created for this problem
        """
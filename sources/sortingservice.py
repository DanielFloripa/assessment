from operator import itemgetter as ig


class Sorting:

    @staticmethod
    def execute(book_list, scenario_rules):
        """
        Service resposible to sort the book_list.
        :param book_list: Books to be sorted
        :param scenario_rules: order or the book list
        :return: book_list: It returns a list of books sorted
        """
        if not scenario_rules:
            return []
        else:
            for rule in scenario_rules:
                if rule[1] == 0:
                    descending = True
                else:
                    descending = False
                book_list = sorted(book_list, key=ig(rule[0]), reverse=descending)
        return book_list

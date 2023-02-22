import unittest
import todo


class TestTodoScript(unittest.TestCase):
    """ Test class """

    def test_print_usage(self):
        """ test usage function """
        msg = todo.print_usage()
        self.assertRegex(todo.print_usage(), '.*Usage: .*')

    # def test_handle_arguments(self):
    #     self.assertEqual(todo.handle_arguments('test.txt', ['./todo.py', 'a', 'a test']),
    #                      'Added: test')

    def test_1a_add_entry(self):
        """ test adding singular word to TODO list """
        self.assertEqual(todo.add_entry('test.txt', 'test'), 'Added: t e s t')


    def test_1b_add_entry(self):
        """ test adding multiple unquoted words to TODO list """
        self.assertEqual(todo.add_entry('test.txt', 'test test'), 
                                        'Added: t e s t   t e s t')


    def test_2a_read_file(self):
        """ test reading TODO list without argument """
        self.assertEqual(todo.read_file('test.txt'), 
                                        ['  1   t e s t', 
                                         '  2   t e s t   t e s t'])


    def test_4a_delete_entry(self):
        """ remove item from TODO list """
        self.assertEqual(todo.delete_entry('test.txt', '1'), 'Removed t e s t')

    def test_4b_delete_invalid_entry(self):
        """ test removing item by giving non-numerical argument """
        self.assertEqual(todo.delete_entry('test.txt', 'apa'), '-- Not a line number --')

    def test_4b_delete_last_entry(self):
        """ remove item from TODO list """
        # we do not test for file removal here. Yet.
        self.assertEqual(todo.delete_entry('test.txt', '1'), 
                                           'Removed t e s t   t e s t')

    def test_5a_read_no_file(self):
        """ test reading TODO list without argument """
        self.assertEqual(todo.read_file('test.txt'), ['<empty list>'])

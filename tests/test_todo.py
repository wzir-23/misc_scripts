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

    def test_1_add_entry(self):
        """ test adding new entry to TODO list """
        self.assertEqual(todo.add_entry('test.txt', 'test'), 'Added: test')


    def test_2a_read_file(self):
        """ test reading TODO list without argument """
        self.assertEqual(todo.read_file('test.txt'), '1   test')


    def test_2b_read_file(self):
        """ test reading TODO list """
        self.assertEqual(todo.read_file('test.txt'), '1   test')


    def test_3_add_entry(self):
        """ test appending entry to TODO list """
        self.assertEqual(todo.add_entry('test.txt', 'test'), 'Added: test')


    def test_4a_delete_entry(self):
        """ test removing item by giving non-numerical argument """
        self.assertEqual(todo.delete_entry('test.txt', 'apa'), '-- Not a line number --')


    def test_4b_delete_entry(self):
        """ remove item from TODO list """
        self.assertEqual(todo.delete_entry('test.txt', '1'), 'Removed test')


    def test_4_delete_entry(self):
        """ remove item from TODO list """
        self.assertEqual(todo.delete_entry('test.txt', '1'), 'Removed test')

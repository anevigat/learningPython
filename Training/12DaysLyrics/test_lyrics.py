from lyrics import *
import unittest


class TestHiker(unittest.TestCase):

    def test_should_print_main_text(self):
        self.assertEqual("On the first day of Christmas,\nMy true love gave to me:\n", print_main_text("first"))
        
    def test_should_iterate_and_print(self):
        self.assertEqual("Two turtle doves and\nA partridge in a pear tree.\n", iterate_and_print(text_list, 2))
        
    def test_should_print_full_verse(self):
        self.assertEqual("On the first day of Christmas,\nMy true love gave to me:\nA partridge in a pear tree.\n", full_verse(text_list, 1))
        
    def test_print_full_verse(self):
        print(iterate_full_verse(text_list))
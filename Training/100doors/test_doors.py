from doors import *
import unittest


class TestDoors(unittest.TestCase):

    def test_should_return_true(self):
        self.assertEqual(True, toggle_boolean(False))

    def test_should_return_false(self):
        self.assertEqual(False, toggle_boolean(True))
    
    def test_should_generate_dictionary_with_closed_doors(self):
        self.assertEqual({"door1": False, "door2": False}, generate_doors(2))
        
    def test_should_iterate_dictionary_1_step(self):
        self.assertEqual([1,2,3,4], iterate_with_steps(4, 1))
        
    def test_should_iterate_dictionary_2_steps(self):
        self.assertEqual([2,4], iterate_with_steps(4, 2))
        
    def test_should_iterate_dictionary_10_steps(self):
        self.assertEqual([10,20], iterate_with_steps(20, 10))
        
    def test_should_toggle_doors_1_step(self):
        self.assertEqual({"door1": True, "door2": True}, toggle_doors({"door1": False, "door2": False}, [1,2]))
        
    def test_should_toggle_doors_2_steps(self):
        self.assertEqual({"door1": False, "door2": True, "door3": False, "door4": True}, toggle_doors({"door1": False, "door2": False, "door3": False, "door4": False}, [2,4]))
        
    def test_full_run(self):
        self.assertEqual({"door1": True, "door2": False, "door3": False, "door4": True}, full_run(4))
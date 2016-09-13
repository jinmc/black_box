from black_box import *
import unittest

class TestBlackBox(unittest.TestCase):

    def setUp(self):
        global real_board
        global printed_board
        global dict
        real_board = create_board()
        printed_board = create_board()
               
    
    def test_create_board(self):
        self.assertEqual(create_board(),
            [ [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False] ])
                
    def test_random_location(self):
        self.assertEqual(4, len(random_location()))

    def test_new_game(self):
        new_game((0, 3), (4, 1), (2, 3), (1, 2))
        self.assertEqual(get_real_board()[0][3], True)  
        self.assertEqual(get_real_board()[4][1], True)

    def test_return_minus(self):
        self.assertEqual(return_minus(True), "* ")
        self.assertEqual(return_minus(False), "- ")

    def test_shoot(self):
        new_game((0, 3), (4, 1), (2, 3), (1, 2))
        self.assertEqual(shoot("1R"), None)
        self.assertEqual(shoot("3T"), "3T")
        self.assertEqual(shoot("4l"), "1T")
        self.assertEqual(shoot("7l"), "7R")


    def test_toggle(self):
        toggle(1, 3)
        self.assertEqual(get_printed_board()[1][3], True)
        self.assertEqual(get_printed_board()[2][4], False)
        toggle(1, 3)
        self.assertEqual(get_printed_board()[1][3], False)
        toggle(0, 7)
        self.assertEqual(get_printed_board()[0][7], True)
        

    def test_score(self):
        new_game((0, 3), (4, 1), (2, 3), (1, 2))
        self.assertEqual(score(), 40)
        shoot("1T")
        dict["1T"] = "a"
        dict["4L"] = "a"
        self.assertEqual(score(), 42)
        toggle(0, 3)
        self.assertEqual(score(), 32)
        

unittest.main()

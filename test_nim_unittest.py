import unittest
import sys

from io import StringIO
from nim import Nim

class TestNim(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        pass

    def tearDown(self):
        pass

    def test_nim_player_move(self):
        nim = Nim(9)
        nim.player_move(2)
        self.assertEqual(nim.player_move(2), 2)

    def test_nim_computer_move_one(self):
        nim = Nim(9)
        nim.computer_move(1)
        output = sys.stdout.getvalue().strip().strip("\n")
        self.assertEqual(output, 'Der Computer nimmt 3 Hölzer.')

    def test_nim_computer_move_two(self):
        nim = Nim(9)
        nim.computer_move(2)
        output = sys.stdout.getvalue().strip().strip("\n")
        self.assertEqual(output, 'Der Computer nimmt 2 Hölzer.')

    def test_nim_computer_move_three(self):
        nim = Nim(9)
        nim.computer_move(3)
        output = sys.stdout.getvalue().strip().strip("\n")
        self.assertEqual(output, 'Der Computer nimmt 1 Hölzer.')

    def test_nim_no_number(self):
        nim = Nim(9)
        nim.player_move('STRING')
        output = sys.stdout.getvalue().strip().strip("\n")
        self.assertEqual(output, 'Du musst eine Zahl eingeben!')

    def test_nim_number_too_big(self):
        nim = Nim(9)
        nim.player_move(4)
        output = sys.stdout.getvalue().strip().strip("\n")
        self.assertEqual(output, 'Du musst zwischen 1 und 3 Hölzer nehmen!')

    def test_nim_number_too_big_edge(self):
        nim = Nim(2)
        nim.player_move(3)
        output = sys.stdout.getvalue().strip().strip("\n")
        self.assertEqual(output, 'Es sind keine 3 Hölzer mehr übrig, bitte nimm weniger!')

    def test_nim_number_too_small(self):
        nim = Nim(9)
        nim.player_move(-1)
        output = sys.stdout.getvalue().strip().strip("\n")
        self.assertEqual(output, 'Du musst zwischen 1 und 3 Hölzer nehmen!')

if __name__ == '__main__':
    unittest.main()
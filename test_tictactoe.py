import unittest
import tictactoe


unittest.TestCase.assertFalse
class Test_TestTictactoe(unittest.TestCase):

    def test_claim_spot(self):
        model = tictactoe.Model(1)

        row_to_claim = 1
        col_to_claim = 2

        expected_value = False

        model.claim_spot(row_to_claim, col_to_claim)

        if not model.is_free_spot(row_to_claim, col_to_claim):
            expected_value = True
        
        self.assertTrue(expected_value)


    def test_is_board_full(self):
        model = tictactoe.Model(1)

        for row in range(3):
            for col in range(3):
                model.claim_spot(row, col)
                model.switch_player()

        self.assertTrue(model.is_board_full())


    def test_switch_player(self):
        model = tictactoe.Model(1)

        first_player = model.player
        model.switch_player()
        second_player = model.player

        self.assertNotEqual(first_player, second_player)


if __name__ == '__main__':
    unittest.main()
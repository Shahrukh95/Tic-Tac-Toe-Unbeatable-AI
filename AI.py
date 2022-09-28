import copy
import random

class AI():
    def __init__(self):
        pass

    # RANDOM AI
    def is_free_spot(self, internal_board, row, col):
        return internal_board[row][col] == 0

    def get_empty_entries(self, internal_board):
        empty_entries = []
        for row in range(3):
            for col in range(3):
                if (self.is_free_spot(internal_board, row, col)):
                    empty_entries.append((row, col))
        return empty_entries

    def get_empty_spot(self, internal_board):
        empty_spots = self.get_empty_entries(internal_board)
        random_number = random.randrange(0, len(empty_spots), 1)
        random_empty_spot = empty_spots[random_number] 
        return random_empty_spot[0], random_empty_spot[1]

    # MINIMAX
    def is_board_full(self, internal_board):
        return not 0 in internal_board
    
    def is_player_win(self, internal_board):
        for col in range(3):
            if internal_board[0][col] == 1 and internal_board[1][col] == 1 and internal_board[2][col] == 1:
                return 1
            if internal_board[0][col] == 2 and internal_board[1][col] == 2 and internal_board[2][col] == 2:
                return 2

        for row in range(3):
            if internal_board[row][0] == 1 and internal_board[row][1] == 1 and internal_board[row][2] == 1:
                return 1
            if internal_board[row][0] == 2 and internal_board[row][1] == 2 and internal_board[row][2] == 2:
                return 2

        if internal_board[2][0] == 1 and internal_board[1][1] == 1 and internal_board[0][2] == 1:
            return 1
        if internal_board[2][0] == 2 and internal_board[1][1] == 2 and internal_board[0][2] == 2:
            return 2

        if internal_board[0][0] == 1 and internal_board[1][1] == 1 and internal_board[2][2] == 1:
            return 1
        if internal_board[0][0] == 2 and internal_board[1][1] == 2 and internal_board[2][2] == 2:
            return 2

        if self.is_board_full(internal_board):
            return 0

        return -1


    def minimax(self, internal_board, maximizing):
        winning_index = self.is_player_win(internal_board)

        if winning_index == 1:
            return 1, ()

        elif winning_index == 2:
            return -1, ()

        elif winning_index == 0:
            return 0, ()

        if maximizing:
            max_score = -2
            point_to_mark = ()
            empty_entries = self.get_empty_entries(internal_board)

            for (row, col) in empty_entries:
                temp_board = copy.deepcopy(internal_board)
                temp_board[row][col] = 1
                score = self.minimax(temp_board, False)[0]
                if score > max_score:
                    max_score = score
                    point_to_mark = (row, col)

            return max_score, point_to_mark

        elif not maximizing:
            min_score = 2
            point_to_mark = ()
            empty_entries = self.get_empty_entries(internal_board)

            for (row, col) in empty_entries:
                temp_board = copy.deepcopy(internal_board)
                temp_board[row][col] = 2
                score = self.minimax(temp_board, True)[0]
                if score < min_score:
                    min_score = score
                    point_to_mark = (row, col)

            return min_score, point_to_mark
    



    
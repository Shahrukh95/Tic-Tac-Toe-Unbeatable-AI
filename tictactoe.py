import random
import pygame, sys
import math
import numpy as np
import AI
import Profiling

class View:
    # SCREEN ADJUSTABLE CONSTANTS
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    BOX_HEIGHT = SCREEN_HEIGHT / 3
    BOX_WIDTH  = SCREEN_WIDTH / 3

    WIDTH_OF_LINES = 15
    COLOR_OF_LINES = (0,0,0)

    CIRCLE_RADIUS = 70
    CIRCLE_COLOR = (0, 0, 255)

    CROSS_COLOR = (127, 132, 135)
    CROSS_WIDTH = 25
    CROSS_SPACE = 55

    ERROR_CROSS_COLOR = (255, 0, 0)
    ERROR_CROSS_SPACE = 30

    WINNING_LINE_COLOR = (255, 0, 0)

    BACKGROUND_COLOR = (255,255,255)
    WINNING_TEXT_COLOR = (0, 255, 0)

    BLACK_COLOR = (0,0,0)

    
    pygame.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)


    # WINDOW SIZE
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BACKGROUND_COLOR)

    def __init__(self):
        pass

    def draw_outer_lines(self):
        pygame.draw.line(View.screen, View.COLOR_OF_LINES, (0,View.BOX_HEIGHT), (View.SCREEN_WIDTH, View.BOX_HEIGHT), View.WIDTH_OF_LINES)
        pygame.draw.line(View.screen, View.COLOR_OF_LINES, (0,(View.SCREEN_HEIGHT - View.BOX_HEIGHT)), (View.SCREEN_WIDTH, (View.SCREEN_HEIGHT - View.BOX_HEIGHT)), View.WIDTH_OF_LINES)

        pygame.draw.line(View.screen, View.COLOR_OF_LINES, (View.BOX_WIDTH,0), (View.BOX_WIDTH, View.SCREEN_HEIGHT), View.WIDTH_OF_LINES)
        pygame.draw.line(View.screen, View.COLOR_OF_LINES, ((View.SCREEN_WIDTH - View.BOX_WIDTH),0), ((View.SCREEN_WIDTH - View.BOX_WIDTH), View.SCREEN_HEIGHT), View.WIDTH_OF_LINES)


    def draw_shapes(self, board_array):
        for row in range(3):
            for col in range(3):
                if board_array[row][col] == 1:
                    pygame.draw.circle( View.screen, View.CIRCLE_COLOR, ((col * View.BOX_WIDTH + (View.SCREEN_WIDTH/6)), (row * View.BOX_HEIGHT + (View.SCREEN_HEIGHT/6))), View.CIRCLE_RADIUS, View.WIDTH_OF_LINES )
                elif board_array[row][col] == 2:
                    pygame.draw.line(View.screen, View.CROSS_COLOR, (col * View.BOX_WIDTH + View.CROSS_SPACE, row * View.BOX_HEIGHT + View.BOX_HEIGHT - View.CROSS_SPACE), (col * View.BOX_WIDTH + View.BOX_WIDTH - View.CROSS_SPACE, row * View.BOX_HEIGHT + View.CROSS_SPACE), View.CROSS_WIDTH)
                    pygame.draw.line(View.screen, View.CROSS_COLOR, (col * View.BOX_WIDTH + View.CROSS_SPACE, row * View.BOX_HEIGHT + View.CROSS_SPACE), (col * View.BOX_WIDTH + View.BOX_WIDTH - View.CROSS_SPACE, row * View.BOX_HEIGHT + View.BOX_HEIGHT - View.CROSS_SPACE), View.CROSS_WIDTH)

    def draw_error_cross(self, row, col):
        pygame.draw.line(View.screen, View.ERROR_CROSS_COLOR, (col * View.BOX_WIDTH + View.ERROR_CROSS_SPACE, row * View.BOX_HEIGHT + View.BOX_HEIGHT - View.ERROR_CROSS_SPACE), (col * View.BOX_WIDTH + View.BOX_WIDTH - View.ERROR_CROSS_SPACE, row * View.BOX_HEIGHT + View.ERROR_CROSS_SPACE), View.CROSS_WIDTH)
        pygame.draw.line(View.screen, View.ERROR_CROSS_COLOR, (col * View.BOX_WIDTH + View.ERROR_CROSS_SPACE, row * View.BOX_HEIGHT + View.ERROR_CROSS_SPACE), (col * View.BOX_WIDTH + View.BOX_WIDTH - View.ERROR_CROSS_SPACE, row * View.BOX_HEIGHT + View.BOX_HEIGHT - View.ERROR_CROSS_SPACE), View.CROSS_WIDTH)


    def draw_top_down_line(self, col):
        posX = col * View.BOX_WIDTH + (View.SCREEN_WIDTH/6)
        pygame.draw.line( View.screen, View.WINNING_LINE_COLOR, (posX, View.WIDTH_OF_LINES), (posX, View.SCREEN_HEIGHT - View.WIDTH_OF_LINES), View.WIDTH_OF_LINES )

    def draw_left_right_line(self, row):
        posY = row * View.BOX_HEIGHT + (View.SCREEN_HEIGHT/6)
        pygame.draw.line( View.screen, View.WINNING_LINE_COLOR, (View.WIDTH_OF_LINES, posY), (View.SCREEN_WIDTH - View.WIDTH_OF_LINES, posY), View.WIDTH_OF_LINES )

    def draw_diagonal_to_top_left(self):
        pygame.draw.line( View.screen, View.WINNING_LINE_COLOR, (View.WIDTH_OF_LINES, View.SCREEN_HEIGHT - View.WIDTH_OF_LINES), (View.SCREEN_WIDTH - View.WIDTH_OF_LINES, View.WIDTH_OF_LINES), View.WIDTH_OF_LINES )

    def draw_diagonal_to_bottom_right(self):
        pygame.draw.line( View.screen, View.WINNING_LINE_COLOR, (View.WIDTH_OF_LINES, View.WIDTH_OF_LINES), (View.SCREEN_WIDTH - View.WIDTH_OF_LINES, View.SCREEN_HEIGHT - View.WIDTH_OF_LINES), View.WIDTH_OF_LINES )

    def print_winning_text(self, is_draw, text_to_show):
        text_surface = self.my_font.render(text_to_show, False, View.WINNING_TEXT_COLOR)
        View.screen.blit(text_surface, ((View.SCREEN_WIDTH/2 - 40), 0)) if is_draw else View.screen.blit(text_surface, ((View.SCREEN_WIDTH/2 - 90), 0))

    def print_game_mode_menu(self):
        text_surface = self.my_font.render("Press 1 for PVP", False, View.BLACK_COLOR)
        View.screen.blit(text_surface, ((View.SCREEN_WIDTH/2 - 100), (View.SCREEN_HEIGHT/2 - 90)))

        text_surface = self.my_font.render("Press 2 for AI", False, View.BLACK_COLOR)
        View.screen.blit(text_surface, ((View.SCREEN_WIDTH/2 - 100), (View.SCREEN_HEIGHT/2 - 40)))

    def print_ai_menu(self):
        text_surface = self.my_font.render("Press 1 for Random AI", False, View.BLACK_COLOR)
        View.screen.blit(text_surface, ((View.SCREEN_WIDTH/2 - 150), (View.SCREEN_HEIGHT/2 - 90)))

        text_surface = self.my_font.render("Press 2 for Unbeatable AI", False, View.BLACK_COLOR)
        View.screen.blit(text_surface, ((View.SCREEN_WIDTH/2 - 150), (View.SCREEN_HEIGHT/2 - 40)))


class Model:
    def __init__(self, player):
        self.internal_board = np.zeros((3,3))
        self.player = player

    def claim_spot(self, row, col):
        self.internal_board[row][col] = self.player

    def is_free_spot(self, row, col):
        return self.internal_board[row][col] == 0

    def is_board_full(self):
        return not 0 in self.internal_board

    def switch_player(self):
        self.player = 1 if self.player % 2 == 0 else 2
        return self.player

    def is_player_win(self, player):
        for col in range(3):
            if self.internal_board[0][col] == player and self.internal_board[1][col] == player and self.internal_board[2][col] == player:
                return True, 'top-down', col

        for row in range(3):
            if self.internal_board[row][0] == player and self.internal_board[row][1] == player and self.internal_board[row][2] == player:
                return True, 'left-right', row

        if self.internal_board[2][0] == player and self.internal_board[1][1] == player and self.internal_board[0][2] == player:
            return True, 'diagonal-to-top-left', 0

        if self.internal_board[0][0] == player and self.internal_board[1][1] == player and self.internal_board[2][2] == player:
            return True, 'diagonal-to-bottom-right', 0

        return False, '', 0

    def get_empty_entries(self):
        empty_entries = []
        for row in range(3):
            for col in range(3):
                if (self.is_free_spot(row, col)):
                    empty_entries.append((row, col))
        
        return empty_entries

    def generate_boards(self, moves_played):
        boards_array = []
        for boards in range(100):
            boards_array.append(np.zeros((3,3)))

            board_remaining_squares = moves_played
            current_player = 1
            for row in range(3):
                for col in range(3):
                    if board_remaining_squares >= 1:
                        boards_array[boards][row][col] = current_player
                        board_remaining_squares -= 1
                        current_player = 1 if current_player == 2 else 2

            random.Random(boards).shuffle(boards_array[boards][0])
            random.Random(boards).shuffle(boards_array[boards][1])
            random.Random(boards).shuffle(boards_array[boards][2])

        return boards_array
        

class Controller:
    def __init__(self):
        self.model = Model(1)
        self.view = View()

        self.is_game_end = False
        self.game_mode = 0
        self.ai_mode = 0


    def check_and_call_line_draw(self, line_direction, row_or_column):
        if line_direction == 'top-down':
            self.view.draw_top_down_line(row_or_column)
        elif line_direction == 'left-right':
            self.view.draw_left_right_line(row_or_column)
        elif line_direction == 'diagonal-to-top-left':
            self.view.draw_diagonal_to_top_left()
        elif line_direction == 'diagonal-to-bottom-right':
            self.view.draw_diagonal_to_bottom_right()


    def draw_winning_board(self, line_direction, row_or_column, isCrossReset):
        self.check_and_call_line_draw(line_direction, row_or_column)
        if isCrossReset:
            self.model.switch_player()
            self.view.print_winning_text(False, f'Player {self.model.player} wins!')
        else:
            self.view.print_winning_text(False, f'Player {self.model.player} wins!')



    def win_or_draw(self):
        winning_boolean, line_direction, row_or_column = self.model.is_player_win(self.model.player)
        if winning_boolean:
            self.is_game_end = True
            self.draw_winning_board(line_direction, row_or_column, False)
        else:
            self.is_game_end = False

        if self.model.is_board_full() and not (self.model.is_player_win(1)[0] or self.model.is_player_win(2)[0]):
            self.view.print_winning_text(True, 'Draw!')
            self.is_game_end = True


    def select_game_mode(self):
         while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 1
                    if event.key == pygame.K_2:
                        return 2
                        
            
            pygame.display.update()


    def initiliaze_menus(self):
        self.view.print_game_mode_menu()
        self.game_mode = self.select_game_mode()
        View.screen.fill(View.BACKGROUND_COLOR)

        self.ai_mode = 0
        if self.game_mode == 2:
            self.view.print_ai_menu()
            self.ai_mode = self.select_game_mode()
            View.screen.fill(View.BACKGROUND_COLOR)


    def run(self):
        self.initiliaze_menus()

        ai_object = AI.AI()
        self.view.draw_outer_lines()

        USER_EVENT = pygame.USEREVENT

        while True:
            for event in pygame.event.get():
                # QUIT APPLICATION HANDLER
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.is_game_end:                    
                    clicked_column = math.floor(event.pos[0] / View.BOX_WIDTH)
                    clicked_row =  math.floor(event.pos[1] / View.BOX_HEIGHT)

                    if self.model.is_free_spot(clicked_row, clicked_column):
                        self.model.claim_spot(clicked_row, clicked_column)
                        self.view.draw_shapes(self.model.internal_board)

                        self.win_or_draw()
                        if self.is_game_end == False:
                            self.model.switch_player()

                        if self.ai_mode == 1:
                            if self.is_game_end == False:                             
                                r_ai_claim_x, r_ai_claim_y = ai_object.get_empty_spot(self.model.internal_board)
                                self.model.claim_spot(r_ai_claim_x, r_ai_claim_y)

                                self.win_or_draw()
                                self.view.draw_shapes(self.model.internal_board)

                                if self.is_game_end == False:
                                    self.model.switch_player()

                        elif self.ai_mode == 2:
                            if self.is_game_end == False:
                                ai_claim_x, ai_claim_y = ai_object.minimax(self.model.internal_board, False)[1]
                                self.model.claim_spot(ai_claim_x, ai_claim_y)

                                self.win_or_draw()
                                self.view.draw_shapes(self.model.internal_board)

                                if self.is_game_end == False:
                                    self.model.switch_player()

                    else:
                        self.view.draw_error_cross(clicked_row, clicked_column)
                        pygame.time.set_timer( USER_EVENT, 600 )
                    

                if event.type == USER_EVENT:
                        self.view.screen.fill(View.BACKGROUND_COLOR)
                        self.view.draw_outer_lines()
                        self.view.draw_shapes(self.model.internal_board)
                        self.win_or_draw()
                        pygame.time.set_timer( USER_EVENT, 0 )
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.model.internal_board.fill(0)
                        View.screen.fill(View.BACKGROUND_COLOR)
                        self.is_game_end = False
                        self.model.player = 1
                        self.initiliaze_menus()
                        self.view.draw_outer_lines()               
            
            pygame.display.update()


if __name__ == '__main__':
    controller_object = Controller()
    controller_object.run()

    # profiling_obj = Profiling.Profiling()
    # profiling_obj.run_profiler("Random AI")
    # profiling_obj.run_profiler("Minimax Algorithm")

import timeit
import tictactoe
import AI

class Profiling():
    def __init__(self):
        pass

    def run_profiler(self, type):
        board_obj = tictactoe.Model(1)
        ai_object = AI.AI()

        for moves_played in range(9):
            random_ai_average_time = 0
            random_ai_experiments_made = 0
            
            for i in range(100):
                current_board = board_obj.generate_boards(moves_played)[i]
                
                start = timeit.default_timer()
                if type == 'Random AI':
                    ai_object.get_empty_spot(current_board)
                elif type == 'Minimax Algorithm':
                    ai_object.minimax(current_board, False)[1]
                end = timeit.default_timer()
                time_taken = format(float(end-start) * 1000, '.12f')

                random_ai_experiments_made += 1
                random_ai_average_time += float(time_taken)

            if (type == 'Random AI'):
                print(f"Benhmark Random AI for {9 - moves_played} remaning squares: {random_ai_average_time/random_ai_experiments_made} ms")
            elif (type == 'Minimax Algorithm'):
                print(f"Minimax Algorithm for {9 - moves_played} remaning squares: {random_ai_average_time/random_ai_experiments_made} ms")
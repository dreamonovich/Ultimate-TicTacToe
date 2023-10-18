FIRST_LETTER = 'X'
ZERO_LETTER = '0'
BOARD_HEIGHT = 3
BOARD_LENGTH = 3

win_combinations = [set((0, 1, 2)), set((3, 4, 5)), set((6, 7, 8)), set((0, 3, 6)),
                    set((1, 4, 7)), set((2, 6, 8)), set((0, 4, 8)), set((2, 4, 6))]
def swap_number_and_letter(var):
    if type(var) is int:
        if var == 0:
            return ZERO_LETTER
        if var == 1:
            return FIRST_LETTER
        if var == -1:
            return ' '
        else:
            return var

    if type(var) is bool:
        if var:
            return ZERO_LETTER
        else:
            return FIRST_LETTER


    return 0 if var == ZERO_LETTER else 1
class Board:
    def __init__(self):



        self.game_pos = [[-1 for _ in range(BOARD_HEIGHT * BOARD_LENGTH)] for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]
        self.inner_first_pos = [
            [], [], [],
            [], [], [],
            [], [], []
        ]
        self.inner_zero_pos = [
            [], [], [],
            [], [], [],
            [], [], []
        ]
        self.outer_first_pos = []
        self.outer_zero_pos = []
        self.inner_end = False
        self.outer_end = False
        self.winner = 0


        self.zero_turn = False

    def main(self):
        self.print_game(preview_mode=True)
        print(f'\nХод {swap_number_and_letter(self.zero_turn)}(внешнее-поле внетреннее-поле): ', end='')
        self.outer_field, self.inner_field = tuple(map(int, input().split()))
        self.game_pos[self.outer_field][self.inner_field] = swap_number_and_letter(swap_number_and_letter(self.zero_turn))
        self.zero_turn = not self.zero_turn
        self.current_field = self.inner_field
        while not self.outer_end:
            while not self.inner_end:
                self.print_game()
                print(f'\nХод {swap_number_and_letter(self.zero_turn)}: ', end='')
                self.outer_field, self.inner_field = tuple(map(int, input().split()))
                if self.outer_field != self.current_field:
                    print('Не то поле')
                    continue
                if self.game_pos[self.outer_field][self.inner_field] != -1:
                    print('Не свободно')
                    continue
                self.game_pos[self.outer_field][self.inner_field] = swap_number_and_letter(swap_number_and_letter(self.zero_turn))
                if self.zero_turn:
                    self.inner_zero_pos[self.current_field].append(self.inner_field)
                    if set(self.outer_zero_pos[self.current_field]) in win_combinations:
                        self.inner_end = True
                        self.winner = ZERO_LETTER
                        self.outer_zero_pos.append(self.current_field)
                else:
                    self.inner_first_pos[self.current_field].append(self.inner_field)
                    if set(self.inner_first_pos[self.current_field]) in win_combinations:
                        self.inner_end = True
                        self.winner = FIRST_LETTER
                        self.outer_first_pos.append(self.current_field)
                self.zero_turn = not self.zero_turn
                self.current_field = self.inner_field

            self.game_pos[self.outer_field] = [-1 for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]
            self.game_pos[self.outer_field][BOARD_HEIGHT * BOARD_LENGTH // 2] = self.winner

            if set(self.outer_first_pos) in win_combinations:
                self.winner = FIRST_LETTER
                self.outer_end = True
            elif set(self.outer_zero_pos) in win_combinations:
                self.winner = ZERO_LETTER
                self.inner_end = True
        self.print_game()
        print(f'Игра окончена, победа {self.winner}')




    def print_game(self, preview_mode=False):
        if preview_mode:
            print("""      |       |       
  0   |   1   |   2   
      |       |       
---------------------
      |       |       
   3  |   4   |   5   
      |       |       
---------------------
      |       |       
   6  |   7   |   8   
      |       |      """)
            return 0
        for i in range(BOARD_HEIGHT):
            for b in range(BOARD_LENGTH):
                for j in range(i * 3, i * 3 + BOARD_LENGTH):
                    for l in range(b * 3, b * 3 + BOARD_LENGTH):
                        print(swap_number_and_letter(self.game_pos[j][l]), end=' ')
                    if j != i * 3 + BOARD_LENGTH - 1:
                        print('|', end=' ')
                print()
            if i != BOARD_HEIGHT - 1:
                print('-------' * BOARD_LENGTH)

board = Board()

if __name__ == '__main__':
    print('короче это типо еркмтики нолики но типо их 9 в каждом поле  правила прочитайте в интернете.\n')
    board.main()

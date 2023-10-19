FIRST_LETTER = 'X'
ZERO_LETTER = '0'
BOARD_HEIGHT = 3
BOARD_LENGTH = 3

win_combinations = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6},
                    {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6})
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
        self.local_first_pos = [
            [], [], [],
            [], [], [],
            [], [], []
        ]
        self.local_zero_pos = [
            [], [], [],
            [], [], [],
            [], [], []
        ]
        self.global_first_pos = []
        self.global_zero_pos = []
        self.local_end = False
        self.global_end = False
        self.winner = 0


        self.zero_turn = False

    def main(self):
        self.print_game(preview_mode=True)
        print(f'\nХод {swap_number_and_letter(self.zero_turn)}(внешнее-поле внетреннее-поле): ', end='')
        while True:
            try:
                self.global_field, self.local_field = tuple(map(int, input().split()))
                self.game_pos[self.global_field][self.local_field] = swap_number_and_letter(
                    swap_number_and_letter(self.zero_turn))
                self.zero_turn = not self.zero_turn
                self.global_field = self.local_field
                break
            except:
                print('Некорректный ввод')
                continue
        while True:
            try:
                while not self.global_end:
                    while not self.local_end:
                        self.print_game()
                        print(f'\nХод {swap_number_and_letter(self.zero_turn)}: ', end='')
                        self.local_field = int(input())
                        if self.game_pos[self.global_field][self.local_field] != -1:
                            print('Не свободно')
                            continue
                        self.game_pos[self.global_field][self.local_field] = swap_number_and_letter(swap_number_and_letter(self.zero_turn))
                        if self.zero_turn:
                            self.local_zero_pos[self.global_field].append(self.local_field)
                            if set(self.local_zero_pos[self.global_field]) in win_combinations:
                                self.local_end = True
                                self.winner = ZERO_LETTER
                                self.global_zero_pos.append(self.global_field)
                        else:
                            self.local_first_pos[self.global_field].append(self.local_field)
                            if set(self.local_first_pos[self.global_field]) in win_combinations:
                                self.local_end = True
                                self.winner = FIRST_LETTER
                                self.global_first_pos.append(self.global_field)
                        self.zero_turn = not self.zero_turn
                        self.global_field = self.local_field

                    self.game_pos[self.global_field] = [-1 for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]
                    self.game_pos[self.global_field][BOARD_HEIGHT * BOARD_LENGTH // 2] = self.winner

                    if set(self.global_first_pos) in win_combinations:
                        self.winner = FIRST_LETTER
                        self.global_end = True
                    elif set(self.global_zero_pos) in win_combinations:
                        self.winner = ZERO_LETTER
                        self.local_end = True
                self.print_game()
                print(f'Игра окончена, победа {self.winner}')
                break
            except:
                print('Некорректный ввод')
                continue




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

FIRST_LETTER = "X"
ZERO_LETTER = "0"
BOARD_HEIGHT = 3
BOARD_LENGTH = 3
WIN_COMBINATIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


class UltimateTicTacToeBoard:
    def __init__(self):
        self.game_pos = [
            [-1 for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]
            for _ in range(BOARD_HEIGHT * BOARD_LENGTH)
        ]

        self.local_zero_pos = [[] for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]
        self.local_first_pos = [[] for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]

        self.global_first_pos = []
        self.global_zero_pos = []

        self.local_end = False
        self.global_end = False

        self.winner = 0

        self.zero_turn = False

    def main(self):
        self.print_board(preview_mode=True)
        print(
            f"\nХод {self.ultimate_tictactoe_swapper(self.zero_turn)}(внешнее-поле внетреннее-поле): ",
            end="",
        )
        while True:
            try:
                self.global_field, self.local_field = tuple(map(int, input().split()))
                self.insert_move_into_list("game_pos")
                self.insert_move_into_list("local_pos")
                self.zero_turn = not self.zero_turn
                self.global_field = self.local_field
                break
            except:
                print("Некорректный ввод")
                continue

        while True:
            try:
                while not self.global_end:
                    while not self.local_end:
                        self.print_board()
                        print(
                            f"\nХод {self.ultimate_tictactoe_swapper(self.zero_turn)}: ",
                            end="",
                        )

                        self.local_field = int(input())

                        if not self.field_is_free():
                            print("Не свободно")
                            continue

                        self.insert_move_into_list("game_pos")
                        self.insert_move_into_list("local_pos")

                        self.zero_turn = not self.zero_turn
                        self.global_field = self.local_field

                        if self.local_or_global_win()[0]:
                            self.local_end = True
                            self.winner = self.local_or_global_win()[1]
                            self.insert_move_into_list("global_pos")

                    self.insert_winner_into_global_pos()

                    if self.local_or_global_win()[0]:
                        self.global_end = True
                        self.winner = self.local_or_global_win()[1]

                self.print_board()

                print(f"Игра окончена, победа {self.winner}")
                break

            except:
                print("Некорректный ввод")
                continue

    def ultimate_tictactoe_swapper(self, var):  # bool->str->num->str
        if type(var) is int:
            if var == 0:
                return ZERO_LETTER
            if var == 1:
                return FIRST_LETTER
            if var == -1:
                return " "
            else:
                return var

        if type(var) is bool:
            if var:
                return ZERO_LETTER
            else:
                return FIRST_LETTER

        return 0 if var == ZERO_LETTER else 1

    def insert_move_into_list(self, list_to_insert):
        if list_to_insert == "game_pos":
            self.game_pos[self.global_field][
                self.local_field
            ] = self.ultimate_tictactoe_swapper(
                self.ultimate_tictactoe_swapper(self.zero_turn)
            )

        if list_to_insert == "local_pos":
            if self.zero_turn:
                self.local_zero_pos[self.global_field].append(self.local_field)

            else:
                self.local_first_pos[self.global_field].append(self.local_field)

        if list_to_insert == "global_pos":
            if self.zero_turn:
                self.global_zero_pos.append(self.global_field)

            else:
                self.global_first_pos.append(self.global_field)

    def local_or_global_win(self):
        if set(self.local_zero_pos[self.global_field]) in WIN_COMBINATIONS:
            return (True, ZERO_LETTER)

        elif set(self.local_first_pos[self.global_field]) in WIN_COMBINATIONS:
            return (True, FIRST_LETTER)

        elif set(self.global_first_pos) in WIN_COMBINATIONS:
            return (True, FIRST_LETTER)

        elif set(self.global_zero_pos) in WIN_COMBINATIONS:
            return (True, FIRST_LETTER)

        else:
            return (False, None)

    def insert_winner_into_global_pos(self):
        self.game_pos[self.global_field] = [
            -1 for _ in range(BOARD_HEIGHT * BOARD_LENGTH)
        ]
        self.game_pos[self.global_field][BOARD_HEIGHT * BOARD_LENGTH // 2] = self.winner

    def field_is_free(self):
        return self.game_pos[self.global_field][self.local_field] == -1

    def print_board(self, preview_mode=False):
        if preview_mode:
            print(
                """
      |       |       
  0   |   1   |   2   
      |       |       
---------------------
      |       |       
   3  |   4   |   5   
      |       |       
---------------------
      |       |       
   6  |   7   |   8   
      |       |      """
            )
            return 0
        for global_index_counter in range(BOARD_HEIGHT):
            for local_index_counter in range(BOARD_LENGTH):
                for global_index in range(
                    global_index_counter * 3, global_index_counter * 3 + BOARD_LENGTH
                ):
                    for local_index in range(
                        local_index_counter * 3, local_index_counter * 3 + BOARD_LENGTH
                    ):
                        print(
                            self.ultimate_tictactoe_swapper(
                                self.game_pos[global_index][local_index]
                            ),
                            end=" ",
                        )
                    if global_index != global_index_counter * 3 + BOARD_LENGTH - 1:
                        print("|", end=" ")
                print()
            if global_index_counter != BOARD_HEIGHT - 1:
                print("-------" * BOARD_LENGTH)


board = UltimateTicTacToeBoard()

if __name__ == "__main__":
    print(
        "короче это типо еркмтики нолики но типо их 9 в каждом поле  правила прочитайте в интернете.\n"
    )
    board.main()

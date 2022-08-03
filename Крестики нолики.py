#компьютер играет в крустики нолики против пользователя
#глобальные константы
x = "X"
o = "O"
empty = " "
tie = "Ничья"
num_squares = 9
def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print("""
    Добро пожаловать 
    Игра ничинается
    Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соотвествуют полям
    доски- так, как показано ниже
     0 | 1 | 2
     3 | 4 | 5
     6 | 7 | 8
     приготовьтесь к игре\n""")
def yes_no(question):
    response= None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
        while response not in (1,2,3,4,5,6,7,8,0):
            response = int(input(question))
    return response

def pieces():
    """Определяет принадлежность первого хода"""
    go_first= yes_no("Хочешь оставть засобой первый ход? (y/n)")
    if go_first=="y":
        print("Ну что ж, дам тебе фору: играй крестиками")
        human = x
        computer = o
    else:
        print("\nТвоя удаль тебя погубит ")
        computer = x
        human = o
    return computer, human
def new_board():
   board = []
   for square in range(num_squares):
        board.append(empty)
   return board
def display_board(board):

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):

    moves = []
    for square in range(num_squares):
        if board[square] == empty:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
        if empty not in board:

            return tie
    return None
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Tвoй ход. Выбери одно из полей (О - 8):", 0, num_squares)
    if move not in legal:
        print("\nCмeшнoй человек! Это поле уже занято. Выбери дpyroe.\n")

    print("Ладно ... ")

    return move

def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 6, 2, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move

        board[move] = empty
    for move in legal_moves(board):
        board[move] = human
    # если следующим ходом может победить человек. блокируем этот ход
        if winner(board) == human:
            print(move)
            return move
    # вь1полнив проверку. отменим внесенные изменения
        board[move] = empty
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def next_turn(turn):

    if turn == x:
        return o
    else:
        return x
def congrat_winner(the_winner, computer, human):
    if the_winner != tie:
        print("Tpи", the_winner, "в ряд!\n")
    else:
        print("Hичья!\n")
    if the_winner == computer:
        print("Kaк я и предсказывал, победа в очередной раз осталась за мной!!!"
              ". \n", "Вот еще один довод в пользу того. что компьютеры превосходят людей решительно во всем.")
    elif the_winner == human:
        print("O нет. этого не может быть! Неужели ты как-то сумел перехитрить меня? \n Клянусь: я, компьютер, не допущу этого больше никогда!")

    elif the_winner == tie:
        print("Teбe несказанно повезло, ты сумел свести игру вничью. \n", "Радуйся же сегодняшнему успеху! Завтра тебе уже не суждено его повторить. ")
def main():
    display_instruct()

    computer, human = pieces()
    turn =x
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
tin = input("Нажмите Enter чтобы выйти \n  Если хочешь попробовать еще раз нажми y, если нет, нажми n ")
while tin == "y":
    main()
    tin = input("Нажмите Enter чтобы выйти \n  Если хочешь попробовать еще раз нажми y ")
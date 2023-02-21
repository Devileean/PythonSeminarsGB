# Function to print the Tic-Tac-Toe
# Функция распечатки поля для игры
def mytictactoe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")


# Function for a single game(функция для одиночной игры) of Tic-Tac-Toe
def singlegame(curplayer):
    # Representing the Tic-Tac-Toe
    val = [' ' for i in range(9)]

    # Storing the positions occupied by X and O
    playerpos = {'X': [], 'O': []}





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


# Defining Function to check Victory
def check_Victory(playerpos, curplayer):
    # All probable winning combinations
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check whether any winning combination is satisfied or not
    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
            # Return True if any winning combination is satisfied
            return True
            # Return False if no combination is satisfied
    return False

# Function for a single game(функция для одиночной игры) of Tic-Tac-Toe
def singlegame(curplayer):
    # Representing the Tic-Tac-Toe
    val = [' ' for i in range(9)]

    # Storing the positions occupied by X and O
    playerpos = {'X': [], 'O': []}

# Defining Function to check if the game is Tied
def check_Tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) == 9:
        return True
    return False


def myscoreboard(scoreboard):
    print("\t--------------------------------")
    print("\t         SCORE BOARD       ")
    print("\t--------------------------------")

    listofplayers = list(scoreboard.keys())
    print("\t   ", listofplayers[0], "\t    ", scoreboard[listofplayers[0]])
    print("\t   ", listofplayers[1], "\t    ", scoreboard[listofplayers[1]])

    print("\t--------------------------------\n")






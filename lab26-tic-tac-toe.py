"""
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X')
into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a
function main that models gameplay taking in user inputs through REPL.

The Player class has the following properties:

name = player name
token = 'X' or 'O'


The Game class has the following properties:

board = your representation of the board
You can represent the board however you like,
such as a 2D list, tuples, or dictionary.


The Game class has the following methods:

__repr__() Returns a pretty string representation of the game board
print(board)
X| |
O|X|O
 | |

move(x, y, player) Place a player's token character string at a given
coordinate (top-left is 0, 0), x is horizontal position,
y is vertical position.
>>> board.move(2, 1, player_1)
 | |
 | |X
 | |

calc_winner() What token character string has won or None if no one has.
X| |
O|X|O
 | |X
>>> board.calc_winner()
X

is_full() Returns true if the game board is full.
X|O|X
X|X|O
O|O|X
>>> board.is_full()
True

is_game_over() Returns true if the game board is full or a player has won.
X|O|X
X|X|O
O|O|X
>>> board.is_game_over()
True

X|O|
 | |X
 | |
>>> board.is_game_over()
False
"""


class Player():
    def __init__(self, name=None, token=None):
        self.name = name
        self.token = token

    def __repr__(self):
        return f"{self.name} is the {self.token} symbol."


class Game():
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def __repr__(self):
        ret = ''
        for row in self.board:
            ret += '|'.join(row) + '\n'
        return ret

    def move(self, x, y, player):
        self.board[y][x] = player.token
        return self.board

    def calc_winner():
        if self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
           return f'{player.token} is the winner!'
        
        elif self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
            return f'{playertoken} is the winner!'
        
        elif self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
            return f'{playertoken} is the winner!'
        
        else:
            None

    def is_full(self):
        pass

    def is_game_over(self):
        pass


p1 = Player('player1', 'X')
p2 = Player('player2', 'O')

print(p1)
print(p2)

game = Game()
game.move(2, 1, p1)
print(game)
game.move(1, 1, p2)
print(game)


# def main():
#     game = Game()


# if __name__ == '__main__':
#     main()

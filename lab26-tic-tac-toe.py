"""
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X')
into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a
function main that models gameplay taking in user inputs through REPL.

1. Remove used position from valid inputs
- replace number position with *
- pop off number from valid inputs
2. Play again?
3. print help/board

"""


class Player():
    def __init__(self, name=None, token=None):
        self.name = name
        self.token = token

    # def __repr__(self):
        # return f"{self.name} is the {self.token} symbol."


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

    def calc_winner(self): # [column][row]

        if self.board[0][0] == self.board[1][0] ==  self.board[2][0] and self.board[0][0] != ' ':
            return f'{self.board[0][0]} is the winner!', True
        
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != ' ':
            return f'{self.board[0][1]} is the winner!', True
        
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ':
            return f'{self.board[0][2]} is the winner!', True

        elif self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ':
            return f'{self.board[0][0]} is the winner!', True

        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ':
            return f'{self.board[1][0]} is the winner!', True
        
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return f'{self.board[0][0]} is the winner!', True

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return f'{self.board[0][2]} is the winner!', True

        else:
            return False

    def is_full(self):
        for row in self.board:
            for i in row:
                if i == ' ':
                    return False
        return True
    

    def is_game_over(self):
        if self.is_full() or self.calc_winner():
            return True
        else:
            return False


def main():
    game = Game()
    valid_inputs = ['1','2','3','4','5','6','7','8','9', 'help', 'h']
    loop = True
    game_board_grid = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    
    board_grid = ''
    for row in game_board_grid:
        board_grid += '|'.join(row) + '\n'
    print("Welcome to Tic-Tac-Toe!" + '\n')

    token1 = input('Player 1 pick a token, x or o: ').strip().lower()
    token2 = ''
    
    if token1 == 'x':
        token2 += 'o'
    else:
        token2 += 'x'
    
    p1 = Player('player1', token1)
    p2 = Player('player2', token2)

    print('\n' + f'Player 2 is {token2} and player 1 is {token1}! Now let\'s play a game.' + '\n')
    print("You can pick from from the following valid positions only:" + '\n' + board_grid)
    print("Print valid positions anytime with: \'(h)elp\' ")

    turn = 0
    while loop:
        valid = False
        player = p1
        
        if turn % 2 == 0:
            player = p1
        else:
            player = p2

        while not valid:
            choice = input(f'make your move {player.name}: ')
            if choice in valid_inputs:
                valid = True
            else:
                print('Invalid input! Pick from a number below')
                print(board_grid)  


        if choice == '1':
            game.move(0,0, player)
            print(game)
        elif choice == '2':
            game.move(1,0, player)
            print(game)
        elif choice == '3':
            game.move(2,0, player)
            print(game)
        elif choice == '4':
            game.move(0,1, player)
            print(game)
        elif choice == '5':
            game.move(1,1, player)
            print(game)
        elif choice == '6':
            game.move(2,1, player)
            print(game)
        elif choice == '7':
            game.move(0,2, player)
            print(game)
        elif choice == '8':
            game.move(1,2, player)
            print(game)
        elif choice == '9':
            game.move(2,2, player)
            print(game)
        elif choice.startswith('h'):
            print('*'*10)
            print(board_grid)
            turn -= 1

        
        if game.is_game_over():
            loop = False
            if game.is_full() and not game.calc_winner():
                print("Rats, it's a scratch!")
                again = input("Would you like to play again? (y/n): ").strip().lower()
                if again.startswith('y'):
                    main()
                elif again.startswith('n'):
                    print("Goodbye!")
                else:   
                    print("Enter yes, no, y, or n only!")

            else:
                print(game.calc_winner())
                again = input("Would you like to play again? (y/n): ").strip().lower()
                if again.startswith('y'):
                    main()
                elif again.startswith('n'):
                    print("Goodbye!")
                else:   
                    print("Enter yes, no, y, or n only!")
        else:
            turn += 1


if __name__ == '__main__':
    main()

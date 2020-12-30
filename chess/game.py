from termcolor import colored
#colored(string, color)

class Game():
    def __init__(self):
        self.board = [[], [], [], [], [], [], [], [], [], [colored('+', 'red')]]
        self.main()

    def main(self):
        self.placePieces()
        self.display()

    def placePieces(self):
        uniDict = {'WHITE' : {'Pawn' : "♙", 'Rook' : "♖", 'Knight' : "♘", 'Bishop' : "♗", 'King' : "♔", 'Queen' : "♕" }, 'BLACK' : {'Pawn' : "♟", 'Rook' : "♜", 'Knight' : "♞", 'Bishop' : "♝", 'King' : "♚", 'Queen' : "♛" }}
        pieces = ['Rook', 'Knight', 'Bishop', 'King', 'Queen', 'Bishop', 'Knight', 'Rook']
        for i in range(8):
            self.board[i+1].insert(0, colored(8 - i, 'red'))
            self.board[1].append(uniDict['WHITE'][pieces[i]])
            self.board[2].append(uniDict['WHITE']['Pawn'])
            self.board[3].append(colored('·', 'blue'))
            self.board[4].append(colored('·', 'blue'))
            self.board[5].append(colored('·', 'blue'))
            self.board[6].append(colored('·', 'blue'))
            self.board[7].append(uniDict['BLACK']['Pawn'])
            self.board[8].append(uniDict['BLACK'][pieces[i]])
            self.board[9].append(colored(chr(ord('`')+(i+1)), 'red'))
        self.board[0] = self.board[9]
        for i in range(9):
            self.board[i+1].append(colored(8 - i, 'red'))
        self.board[0][9] = colored('+', 'red')


    def display(self):
        print('\n')
        for row in self.board:
            for i in row:
                print(i, end="   ")
            print('\n')

Game()

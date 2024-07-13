import os
from colorama import Fore

class Empty:
    def __init__(self):
        return

    def __repr__(self):
        return "□"


class Piece:
    def __init__(self, position: (str, int)):
        self.position = position
    
    def __repr__(self):
        return "?"

class Board:
    def __init__(self, selection: (str, int), selectionColor: int = Fore.CYAN):
        self.positions = {
            "A": [],
            "B": [],
            "C": [],
            "D": [],
            "E": [],
            "F": [],
            "G": [],
            "H": []
        }
        self.selection = selection
        self.selectionColor = selectionColor

        for key in self.positions:
            for x in range(8):
                self.positions[key].append(Empty())
        
    def add_piece(self, piece: Piece):
        letter = piece.position[0]
        number = piece.position[1]
        self.positions[letter][number - 1] = piece

    def refresh(self):
        os.system("clear")
        
        
        def print_letters():
            line = "  "
            for letter in self.positions:
                line += f"{letter} "

            print(line)
        
        print_letters()

        board = ""

        for i in range(8):
            board += f"{i + 1} "
            for letter in self.positions:
                color = Fore.WHITE
                piece = self.positions[letter][i]
                
                if (letter, i + 1) == self.selection:
                    color = self.selectionColor
                
                board += color + piece.__repr__() + " "

            board += f"{i + 1} "
            if i < 7:
                board += "\n"

        print(board)

        print_letters()

        print()

            

        



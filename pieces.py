import os
from colorama import Fore

def check_letter(letter: str) -> bool:
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for let in letters:
        if letter == let: return True
    return False

class Empty:
    def __init__(self):
        self.color = Fore.RESET
        

    def __repr__(self):
        return "□"


class Piece:
    def __init__(self, position: (str, int), color: str):
        self.position = position
        self.color = color
    
    def __repr__(self):
        return "?"

class Board:
    def __init__(self, selection: (str, int), selectionColor: str = Fore.CYAN):
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
            line = f"{Fore.WHITE}  "
            for letter in self.positions:
                line += f"{letter} "

            print(line)
        
        print_letters()

        board = ""

        for i in range(8):
            board += f"{Fore.WHITE}{i + 1} "
            for letter in self.positions:
                
                piece = self.positions[letter][i]
                
                color = piece.color
                
                if (letter, i + 1) == self.selection:
                    color = self.selectionColor
                
                board += color + piece.__repr__() + " "

            board += f"{Fore.WHITE}{i + 1} "
            if i < 7:
                board += "\n"

        print(board)

        print_letters()

        print()

            
class Pawn(Piece):
    def __init__(self, position: (str, int), color: str):
        super().__init__(position=position, color=color)

    def __repr__(self) -> str:
        return "♟"

class Castle(Piece):
    def __init__(self, position: (str, int), color: str):
        super().__init__(position=position, color=color)

    def __repr__(self) -> str:
        return "♜"

class Knight(Piece):
    def __init__(self, position: (str, int), color: str):
        super().__init__(position=position, color=color)

    def __repr__(self) -> str:
        return "♞"

class Bishop(Piece):
    def __init__(self, position: (str, int), color: str):
        super().__init__(position=position, color=color)

    def __repr__(self) -> str:
        return "♝"

class King(Piece):
    def __init__(self, position: (str, int), color: str):
        super().__init__(position=position, color=color)

    def __repr__(self) -> str:
        return "♚"

class Queen(Piece):
    def __init__(self, position: (str, int), color: str):
        super().__init__(position=position, color=color)

    def __repr__(self) -> str:
        return "♛"

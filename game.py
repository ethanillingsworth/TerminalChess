from pieces import *
from colorama import Fore


selection = ("A", 2)
board = Board(selection=selection)
current_color = Fore.LIGHTBLACK_EX
# Black

# Castles
board.add_piece(Castle(position=("A", 1), color=current_color))
board.add_piece(Castle(position=("H", 1), color=current_color))

# Knights
board.add_piece(Knight(position=("B", 1), color=current_color))
board.add_piece(Knight(position=("G", 1), color=current_color))

# Bishop
board.add_piece(Bishop(position=("C", 1), color=current_color))
board.add_piece(Bishop(position=("F", 1), color=current_color))

# King & Queen
board.add_piece(King(position=("E", 1), color=current_color))
board.add_piece(Queen(position=("D", 1), color=current_color))

# Pawns
board.add_piece(Pawn(position=("A", 2), color=current_color))
board.add_piece(Pawn(position=("B", 2), color=current_color))
board.add_piece(Pawn(position=("C", 2), color=current_color))
board.add_piece(Pawn(position=("D", 2), color=current_color))
board.add_piece(Pawn(position=("E", 2), color=current_color))
board.add_piece(Pawn(position=("F", 2), color=current_color))
board.add_piece(Pawn(position=("G", 2), color=current_color))
board.add_piece(Pawn(position=("H", 2), color=current_color))

current_color = Fore.WHITE
# White

# Castles
board.add_piece(Castle(position=("A", 8), color=current_color))
board.add_piece(Castle(position=("H", 8), color=current_color))

# Knights
board.add_piece(Knight(position=("B", 8), color=current_color))
board.add_piece(Knight(position=("G", 8), color=current_color))

# Bishop
board.add_piece(Bishop(position=("C", 8), color=current_color))
board.add_piece(Bishop(position=("F", 8), color=current_color))

# King & Queen
board.add_piece(King(position=("E", 8), color=current_color))
board.add_piece(Queen(position=("D", 8), color=current_color))

# Pawns
board.add_piece(Pawn(position=("A", 7), color=current_color))
board.add_piece(Pawn(position=("B", 7), color=current_color))
board.add_piece(Pawn(position=("C", 7), color=current_color))
board.add_piece(Pawn(position=("D", 7), color=current_color))
board.add_piece(Pawn(position=("E", 7), color=current_color))
board.add_piece(Pawn(position=("F", 7), color=current_color))
board.add_piece(Pawn(position=("G", 7), color=current_color))
board.add_piece(Pawn(position=("H", 7), color=current_color))

while True:
    
    board.refresh()

    print(f"Selected Piece: {Fore.YELLOW}{selection[0]}-{selection[1]}")
    print(f"{Fore.GREEN}1. Select Piece    Q. Quit")

    inp = input(f"{Fore.BLUE}>>{Fore.WHITE} ")

    if inp == "1":
        letter = input("Letter: ")
        number = input("Number: ")

        if (int(number) > 0 and int(number) < 9) and (check_letter(letter)):
            selection = (letter, number)
            board.selection = (letter, int(number))
        

    elif inp == "q" or inp == "Q":
        quit()
    else:
        print("Invalid choice")
        input()

    

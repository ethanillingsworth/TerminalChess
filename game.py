from pieces import *
from colorama import Fore

print(Fore.WHITE)
selection = ("A", 1)
board = Board(selection=selection)

random_piece = Piece(position=("A", 2))

board.add_piece(random_piece)

while True:
    board.refresh()
    print(f"Selected Piece: {Fore.YELLOW}{selection[0]}-{selection[1]}")
    print(f"{Fore.GREEN}1. Select Piece    Q. Quit")

    inp = input(f"{Fore.BLUE}>>{Fore.WHITE} ")

    if inp == "1":
        letter = input("Letter: ")
        number = input("Number: ")
    elif inp == "q" or inp == "Q":
        quit()
    else:
        print("Invalid choice")
        input()

    

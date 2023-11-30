import PySimpleGUI as Sg
from random import randint


# Function to read the current high score from a text file.

# Buttons to Add to the Board.

# Function to mix the board in a manner it can be solved.

# Function to check for win condition

# Function to swap numbers

# Function called when player wins

# Function to update the high score

# Game Loop

def try_move_number(x =-1, y =-1):
    if x == -1:
        pass #Todo Replace x and y with value from button click.





label = Sg.Text("Move Count: \tHigh Score: ")
cell_0_0 = Sg.Button("Add", key=(0, 0))

# Initialize the number grid.
cells = []
for num in range(0, 17):
    y = num % 4
    x = num // 4
    cells.append(Sg.Button(button_text=str(num+1), key=(x, y), size=(6, 6)))
window = Sg.Window("15 Puzzle", layout=[[label],
                                        [cells[0], cells[1], cells[2], cells[3]],
                                        [cells[4], cells[5], cells[6], cells[7]],
                                        [cells[8], cells[9], cells[10], cells[11]],
                                        [cells[12], cells[13], cells[14], cells[15]]
                                        ])
cells[15].ButtonText = ""

# mix the grid using 15 puzzle rules so the board is solvable.
for _ in range(5000):
    try_move_number(x=randint(0,3),y=randint(0,3)


while True:
    print(window.read())



window.close()

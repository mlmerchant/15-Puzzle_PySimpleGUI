import PySimpleGUI as Sg
from random import randint


def try_move_number(x, y):
    # Check all four directions.
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        check_y = y + direction[0]
        check_x = x + direction[1]

        # Exceeds bounds?
        if check_y < 1 or check_y > 4:
            continue
        if check_x < 1 or check_x > 4:
            continue

        # Convert to position in flat array
        index_to_check = ((check_y - 1) * 4) + check_x - 1

        # print("Index to Check: ", index_to_check)

        if cells[index_to_check].ButtonText == "":
            # print("Found you!")
            current_index = ((y - 1) * 4) + x - 1
            cells[index_to_check].ButtonText = cells[current_index].ButtonText
            cells[current_index].ButtonText = ""
            break


def update_board():
    for cell in cells:
        key = cell.Key
        new_text = cell.ButtonText
        window[key].update(new_text)


label = Sg.Text("Move Count: \tHigh Score: ")
cell_0_0 = Sg.Button("Add", key=(0, 0))

# Initialize the number grid.
cells = []
for num in range(0, 16):
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
#for _ in range(5000):
#    try_move_number(x=randint(1, 4), y=randint(1, 4))


while True:
    selection = window.read()
    print(selection)
    try_move_number(y=selection[0][0] + 1, x=selection[0][1] + 1)
    update_board()
    window.refresh()


window.close()

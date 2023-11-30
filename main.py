import PySimpleGUI as Sg
from random import randint
import time


def simple_alert_box(text):
    Sg.Popup(text, title="", keep_on_top=True, button_type=Sg.POPUP_BUTTONS_OK)


def start_new_game(current_record):
    game_turns = 0

    def try_move_number(x, y):
        global is_processing_click
        is_processing_click = True
        """Swaps valid tiles and returns a 1"""
        current_index = ((y - 1) * 4) + x - 1
        if cells[current_index].ButtonText == "":
            is_processing_click = False
            return 0
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
            if cells[index_to_check].ButtonText == "":
                cells[index_to_check].ButtonText = cells[current_index].ButtonText
                cells[current_index].ButtonText = ""
                is_processing_click = False
                return 1
        is_processing_click = False
        return 0

    def is_winning_board():
        valid_number = 1
        for cell in cells:
            if not str(valid_number) == cell.ButtonText:
                return False
            if valid_number == 15:
                return True
            valid_number += 1

    def update_board():
        for cell in cells:
            key = cell.Key
            new_text = cell.ButtonText
            window[key].update(new_text)

    label = Sg.Text(f"Move Count: {game_turns} \t\tCurrent Record: {current_record}", key="ScoreText")

    # Initialize the number grid.
    cells = []
    for num in range(0, 16):
        y = num % 4
        x = num // 4
        cells.append(Sg.Button(button_text=str(num + 1), key=(x, y), size=(6, 6)))
    window = Sg.Window("15 Puzzle", layout=[[label],
                                            [cells[0], cells[1], cells[2], cells[3]],
                                            [cells[4], cells[5], cells[6], cells[7]],
                                            [cells[8], cells[9], cells[10], cells[11]],
                                            [cells[12], cells[13], cells[14], cells[15]]
                                            ])
    cells[15].ButtonText = ""

    # Mix the grid using 15 puzzle rules so the board is solvable.
    for _ in range(5000):
        try_move_number(x=randint(1, 4), y=randint(1, 4))

    global is_processing_click
    is_processing_click = False
    # Game Loop
    while True:
        selection = window.read()
        time.sleep(.1)
        try:
            if not is_processing_click:
                game_turns += try_move_number(y=selection[0][0] + 1, x=selection[0][1] + 1)
                window[label.Key].update(f"Move Count: {game_turns} \t\tCurrent Record: {current_record}")
        except TypeError:
            exit(0)  # If closed using the x button.
        if not is_processing_click:
            update_board()
            window.refresh()
            if is_winning_board():
                simple_alert_box(f"You won in {game_turns} moves!")
                if game_turns < current_record:
                    simple_alert_box(f"New Lowest Record!")
                window.close()
                return game_turns  # Game ends and returns final score.
            else:
                continue


while True:
    # Hacky way to keep the game from crashing when you spam clicks.
    is_processing_click = False
    try:
        with open("record", "r") as file:
            current_record = int(file.readline())
    except FileNotFoundError:
        with open("record", "w") as file:
            file.write("0")
            current_record = 1000

    turns = start_new_game(current_record)

    if turns < current_record:
        with open("record", "w") as file:
            file.write(str(turns))

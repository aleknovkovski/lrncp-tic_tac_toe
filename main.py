# Functions init

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def are_numbers(coordinates):
    # Create list of booleans for each coordinate, true if digit, false if not
    coordinates_are_numbers = [coordinate in digits for coordinate in coordinates]

    # Return true if all coordinates are digits
    if all(coordinates_are_numbers):
        return True
    else:
        return False


def are_in_range(coordinates):
    coordinate_x = coordinates[0]
    coordinate_y = coordinates[1]
    allowed_range = range(1, 4)

    if coordinate_x in allowed_range and coordinate_y in allowed_range:
        return True
    else:
        return False


def print_matrix():
    print("---------")
    print(f"| {' '.join(row_1)} |")
    print(f"| {' '.join(row_2)} |")
    print(f"| {' '.join(row_3)} |")
    print("---------")


def has_empty_cells():
    grid = [row_1, row_2, row_3]

    for row in grid:
        for item in row:
            if item == " ":
                return True


def check_winner():
    global winner
    global game_over

    # Define lines that constitute a win
    column_1 = [row_1[0], row_2[0], row_3[0]]
    column_2 = [row_1[1], row_2[1], row_3[1]]
    column_3 = [row_1[2], row_2[2], row_3[2]]
    left_diagonal = [row_1[0], row_2[1], row_3[2]]
    right_diagonal = [row_3[0], row_2[1], row_1[2]]

    # Define array/list that contains all the lines
    all_lines = [row_1, row_2, row_3, column_1, column_2, column_3, left_diagonal, right_diagonal]

    # Check if any of the lines has 3 equal items
    for line in all_lines:
        if line[0] == line[1] == line[2]:
            # found a winning line, declare game over, declare winner

            if line[0] == "X":
                winner = "X wins"
                game_over = True
            if line[0] == "O":
                winner = "O wins"
                game_over = True

        # no winning line, but all cells are filled, declare game over
        elif not has_empty_cells():
            game_over = True


def make_a_move():
    valid_move = False
    grid = [row_1, row_2, row_3]

    while not valid_move:
        coordinates = input("Enter the coordinates: ").split()
        if are_numbers(coordinates):

            # If numbers, convert to list of integers
            coordinates = [int(coordinate) for coordinate in coordinates]

            if are_in_range(coordinates):

                # If coordinates in range, define as grid index numbers
                # For example, coordinates "1 2" is the same as grid[0][1]

                move_x = coordinates[0] - 1
                move_y = coordinates[1] - 1

                # If cell empty, fill-in, otherwise print error
                if grid[move_x][move_y] == " ":
                    grid[move_x][move_y] = current_player
                    valid_move = True
                    switch_player()
                    check_winner()
                    print_matrix()
                else:
                    print("This cell is occupied! Choose another one!")
                    valid_move = False

            # If the coordinates are not in range
            else:
                print("Coordinates should be from 1 to 3!")

        # If the coordinates are not valid digits
        else:
            print("You should enter numbers!")


# Initialize variables
game_over = False
winner = "Draw"
current_player = "X"

# Initialize empty rows

row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]

# > Game Time
print_matrix()

print("You enter a move by giving coordinates as 'x y'")
print("We are playing on a 3x3 grid of 9 cells total")
print("So upper most left cell is 1 1, bottom right is 3 3")
print("First to go is Player X")

while has_empty_cells() and not game_over:
    make_a_move()

print(winner)
